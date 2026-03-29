# SchemeConnect AI 🏛️

> **AI-powered Government Welfare Scheme Finder** — Built for Google Solution Challenge 2026

## 🎯 Problem Statement
India has **700+ government welfare schemes** worth lakhs of rupees, but most citizens don't know which ones they qualify for. Billions in welfare money goes unclaimed every year.

**UN SDG Alignment:** SDG 1 (No Poverty) & SDG 10 (Reduced Inequalities)

## ✨ Solution
SchemeConnect AI asks users a few simple questions about themselves (age, income, occupation, etc.) and instantly matches them with **all eligible government schemes** using AI-powered analysis.

## 🛠️ Tech Stack
| Technology | Purpose |
|-----------|---------|
| **Google Gemini AI** | Personalized recommendations & AI chat |
| **Python + FastAPI** | Backend API server |
| **HTML + CSS + JavaScript** | Frontend (single-page app) |

## 🚀 Features
- **Smart Profile Form** — Multi-step form with validation
- **AI-Powered Matching** — Matches users against 22+ real government schemes
- **Personalized AI Summary** — Gemini AI generates tailored recommendations
- **AI Chat Assistant** — Ask follow-up questions about any scheme
- **Detailed Scheme Cards** — Benefits, documents needed, how to apply, official links
- **Responsive Design** — Works on mobile and desktop

## 📋 Schemes Covered
PM Kisan, Ayushman Bharat, PM Awas Yojana, Sukanya Samriddhi, PM Mudra Yojana, Atal Pension Yojana, Stand Up India, PM Vishwakarma, National Scholarship Portal, PM Kaushal Vikas Yojana, and 12+ more.

## 💻 Setup & Run

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/SchemeConnect.git
cd SchemeConnect

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .env file with your Gemini API key
echo "GEMINI_API_KEY=your_key_here" > .env

# 4. Run the server
python main.py

# 5. Open http://localhost:8000 in your browser
```

## 🔑 Get a Gemini API Key
1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Click "Create API Key"
3. Copy the key and paste it in `.env`

## 📁 Project Structure
```
SchemeConnect/
├── main.py              # FastAPI backend + Gemini AI
├── schemes_data.py      # Database of 22+ government schemes
├── requirements.txt     # Python dependencies
├── .env                 # API keys (not in git)
├── .env.example         # Environment template
├── README.md            # This file
└── static/
    ├── index.html       # Single-page application
    ├── css/style.css    # Premium dark theme
    └── js/app.js        # Frontend logic
```

## 🏆 Google Solution Challenge 2026
This project was built for the Google Solution Challenge 2026, organized by Google Developer Groups on Campus.

**Team:** Solo  
**SDGs:** #1 No Poverty, #10 Reduced Inequalities  
**Google Tech Used:** Gemini AI (gemini-2.0-flash)

---

Built with ❤️ for India
