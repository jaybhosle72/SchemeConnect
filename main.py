"""
SchemeConnect AI - Backend Server
Google Solution Challenge 2026
Helps Indian citizens discover government welfare schemes they're eligible for.
Powered by Google Gemini AI.
"""

import os
import sys
import asyncio

# Fix Windows console encoding for Unicode
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional, List
from google import genai
from google.genai import types
from dotenv import load_dotenv
from schemes_data import SCHEMES, INDIAN_STATES

# Load environment variables (from .env file if it exists, otherwise from system env)
load_dotenv(override=False)

# Initialize FastAPI
app = FastAPI(
    title="SchemeConnect AI",
    description="AI-powered Government Welfare Scheme Finder",
    version="1.0.0"
)

# CORS for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Gemini AI (new google-genai SDK)
api_key = os.getenv("GEMINI_API_KEY")
client = None
if api_key and api_key != "your_gemini_api_key_here":
    client = genai.Client(api_key=api_key)
    print(f"[OK] Gemini AI connected! Key starts with: {api_key[:10]}...")
else:
    print(f"[WARNING] GEMINI_API_KEY not found or invalid. Got: '{api_key}'")

# Models to try in order (fallback chain)
MODEL_CHAIN = ["gemini-2.0-flash-lite", "gemini-2.0-flash"]

def call_gemini_fast(prompt: str, max_tokens: int = 300) -> str:
    """Call Gemini API with quick model fallback. No long waits."""
    for model_name in MODEL_CHAIN:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.7,
                    max_output_tokens=max_tokens,
                )
            )
            return response.text
        except Exception as e:
            print(f"[{model_name}] Error: {e}")
            continue
    return None


# =================== DATA MODELS ===================

class UserProfile(BaseModel):
    name: str = "User"
    age: int
    gender: str          # male, female, other
    state: str
    category: str        # general, obc, sc, st
    occupation: str      # farmer, student, business, self-employed, salaried, unemployed, homemaker
    annual_income: int
    disability: bool = False
    education: str = "graduate"     # none, primary, secondary, graduate, postgraduate
    has_land: bool = False
    marital_status: str = "single"  # single, married, widowed, divorced
    has_bank_account: bool = True

class ChatRequest(BaseModel):
    message: str
    context: Optional[str] = None


# =================== SCHEME MATCHING ENGINE ===================

def check_eligibility(scheme: dict, profile: UserProfile) -> tuple:
    """Check if a user profile matches scheme eligibility. Returns (is_eligible, reasons)."""
    eligibility = scheme["eligibility"]
    reasons = []
    disqualified = False

    # Check age range
    if "min_age" in eligibility and profile.age < eligibility["min_age"]:
        disqualified = True
    if "max_age" in eligibility and profile.age > eligibility["max_age"]:
        disqualified = True
    if not disqualified and ("min_age" in eligibility or "max_age" in eligibility):
        min_a = eligibility.get("min_age", 0)
        max_a = eligibility.get("max_age", 150)
        reasons.append(f"Your age ({profile.age}) is within eligible range ({min_a}-{max_a})")

    if disqualified:
        return False, []

    # Check gender
    if "gender" in eligibility and eligibility["gender"] != "all":
        if eligibility["gender"] != profile.gender:
            return False, []
        reasons.append(f"This scheme is for {eligibility['gender']} applicants")

    # Check category (caste)
    if "categories" in eligibility:
        if profile.category not in eligibility["categories"]:
            return False, []
        reasons.append(f"Your category ({profile.category.upper()}) is eligible")

    # Check income
    if "max_income" in eligibility:
        if profile.annual_income > eligibility["max_income"]:
            return False, []
        reasons.append(f"Income within the limit of Rs.{eligibility['max_income']:,}")

    # Check occupation
    if "occupations" in eligibility:
        if profile.occupation not in eligibility["occupations"]:
            return False, []
        reasons.append(f"Your occupation ({profile.occupation}) matches")

    # Check land ownership (for farm schemes)
    if "has_land" in eligibility and eligibility["has_land"]:
        if not profile.has_land:
            return False, []
        reasons.append("You own agricultural land")

    # Check bank account
    if "has_bank_account" in eligibility and eligibility["has_bank_account"]:
        if not profile.has_bank_account:
            return False, []
        reasons.append("You have a bank account")

    # Check state restriction
    if "states" in eligibility:
        if profile.state not in eligibility["states"]:
            return False, []
        reasons.append(f"Available in {profile.state}")

    return True, reasons


# =================== API ENDPOINTS ===================

@app.post("/api/find-schemes")
async def find_schemes(profile: UserProfile):
    """Find all eligible government schemes for the user's profile."""
    matched_schemes = []

    for scheme in SCHEMES:
        is_eligible, reasons = check_eligibility(scheme, profile)
        if is_eligible:
            matched_schemes.append({
                "id": scheme["id"],
                "name": scheme["name"],
                "short_name": scheme["short_name"],
                "category": scheme["category"],
                "icon": scheme["icon"],
                "description": scheme["description"],
                "benefits": scheme["benefits"],
                "potential_benefit_amount": scheme["potential_benefit_amount"],
                "documents": scheme["documents"],
                "how_to_apply": scheme["how_to_apply"],
                "official_link": scheme["official_link"],
                "match_reasons": reasons,
            })

    # Get AI-powered personalized summary
    ai_summary = await generate_ai_summary(profile, matched_schemes)

    return {
        "total_found": len(matched_schemes),
        "schemes": matched_schemes,
        "ai_summary": ai_summary,
        "profile_name": profile.name,
    }


async def generate_ai_summary(profile: UserProfile, schemes: list) -> str:
    """Use Gemini to generate a personalized recommendation summary."""
    if not client:
        if not schemes:
            return "No matching schemes found based on your profile. Try adjusting your details - you may be eligible for more schemes than you think!"
        scheme_names = [s["name"] for s in schemes[:5]]
        return f"Great news, {profile.name}! You're eligible for {len(schemes)} government schemes including {', '.join(scheme_names[:3])}. Review each scheme below and start applying today!"

    scheme_details = "\n".join([
        f"- {s['name']}: {s['benefits']}" for s in schemes[:8]
    ])

    prompt = f"""You are SchemeConnect AI, a warm and helpful assistant for Indian citizens.
    
A user named {profile.name} just searched for government schemes. Their profile:
- Age: {profile.age}, Gender: {profile.gender}
- State: {profile.state}, Category: {profile.category}
- Occupation: {profile.occupation}, Annual Income: Rs.{profile.annual_income:,}
- Education: {profile.education}

They are eligible for {len(schemes)} schemes:
{scheme_details if schemes else "No schemes matched."}

Write a brief, warm, personalized 3-4 sentence recommendation in simple English.
- Address them by name
- Highlight the top 2-3 most valuable schemes and their key monetary benefits
- Be encouraging and mention the total potential benefits they could receive
- End with a motivating call-to-action
- Keep it under 120 words
- Do NOT use markdown formatting, bullet points, or asterisks - write in plain flowing text."""

    result = call_gemini_fast(prompt, max_tokens=300)
    if result:
        return result
    # Instant fallback - no waiting
    if schemes:
        top_schemes = [s['name'] for s in schemes[:3]]
        return f"Great news, {profile.name}! You're eligible for {len(schemes)} government schemes including {', '.join(top_schemes)}. Check out the details below to see your benefits, required documents, and how to apply. Don't miss out - start your applications today!"
    return "No matching schemes found based on your profile. Try adjusting your details - you may be eligible for more schemes than you think!"


@app.post("/api/chat")
async def chat_endpoint(req: ChatRequest):
    """AI chat for follow-up questions about government schemes."""
    if not client:
        return {"response": "AI is currently in fallback mode. Please configure your GEMINI_API_KEY in the .env file to enable AI chat."}

    prompt = f"""You are SchemeConnect AI, a friendly, knowledgeable assistant that helps Indian citizens understand and apply for government welfare schemes.

Rules:
- Answer in simple, clear English that anyone can understand
- Be warm, encouraging, and supportive
- If the user asks about a specific scheme, provide accurate details about eligibility, benefits, and how to apply
- If you're unsure about exact details, recommend visiting the official government website
- Keep responses concise (under 200 words)
- Mention relevant schemes they might not know about
- Do NOT use markdown formatting or asterisks - write in plain text with natural paragraphs
- Use numbers and amounts with Rs. symbol where appropriate

{f"Context about user's profile and matched schemes: {req.context}" if req.context else ""}

User's question: {req.message}"""

    result = call_gemini_fast(prompt, max_tokens=500)
    if result:
        return {"response": result}
    return {"response": "I'm sorry, the AI service is temporarily busy. The Gemini API free tier has a limit of 15 requests per minute. Please wait about 30 seconds and try again!"}


@app.get("/api/states")
async def get_states():
    """Return list of Indian states for the form dropdown."""
    return {"states": INDIAN_STATES}


@app.get("/api/schemes/all")
async def get_all_schemes():
    """Return all available schemes (for browsing)."""
    return {"schemes": SCHEMES, "total": len(SCHEMES)}


# =================== SERVE FRONTEND ===================

@app.get("/")
async def serve_index():
    """Serve the main application page."""
    return FileResponse("static/index.html")

# Mount static assets (CSS, JS) - MUST be after the "/" route
app.mount("/static", StaticFiles(directory="static"), name="static")


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    print(f"\nSchemeConnect AI is starting on port {port}...")
    print(f"Open http://localhost:{port} in your browser\n")
    uvicorn.run(app, host="0.0.0.0", port=port)
