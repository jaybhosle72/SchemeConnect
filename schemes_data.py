# SchemeConnect AI — Comprehensive Indian Government Schemes Database
# Each scheme contains real eligibility criteria for accurate matching

SCHEMES = [
    # ─────────────────── AGRICULTURE ───────────────────
    {
        "id": "pm-kisan",
        "name": "PM Kisan Samman Nidhi",
        "short_name": "PM-KISAN",
        "category": "Agriculture",
        "icon": "🌾",
        "description": "Direct income support of ₹6,000 per year to farmer families, paid in three equal installments of ₹2,000 every four months.",
        "benefits": "₹6,000/year (₹2,000 every 4 months) directly to bank account",
        "eligibility": {
            "occupations": ["farmer"],
            "has_land": True,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Aadhaar Card", "Bank Account Details", "Land Ownership Records"],
        "how_to_apply": "Visit pmkisan.gov.in or nearest CSC center. Register with Aadhaar and land details.",
        "official_link": "https://pmkisan.gov.in",
        "potential_benefit_amount": "₹6,000/year"
    },

    # ─────────────────── HEALTH ───────────────────
    {
        "id": "ayushman-bharat",
        "name": "Ayushman Bharat PM-JAY",
        "short_name": "PMJAY",
        "category": "Health",
        "icon": "🏥",
        "description": "World's largest health insurance scheme providing ₹5 lakh per family per year for secondary and tertiary hospitalization.",
        "benefits": "₹5,00,000/year health cover for hospitalization, surgeries, and treatments at empanelled hospitals",
        "eligibility": {
            "max_income": 300000,
            "categories": ["obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Aadhaar Card", "Ration Card", "Income Certificate"],
        "how_to_apply": "Check eligibility at mera.pmjay.gov.in using Aadhaar or ration card number. Get Ayushman card at nearest empanelled hospital or CSC.",
        "official_link": "https://pmjay.gov.in",
        "potential_benefit_amount": "₹5,00,000/year"
    },
    {
        "id": "pmjjby",
        "name": "PM Jeevan Jyoti Bima Yojana",
        "short_name": "PMJJBY",
        "category": "Health",
        "icon": "🛡️",
        "description": "Life insurance coverage of ₹2 lakh at just ₹436/year premium. Covers death due to any reason.",
        "benefits": "₹2,00,000 life insurance cover at ₹436/year premium",
        "eligibility": {
            "min_age": 18,
            "max_age": 50,
            "has_bank_account": True,
            "gender": "all",
            "categories": ["general", "obc", "sc", "st"]
        },
        "documents": ["Aadhaar Card", "Bank Account with auto-debit consent"],
        "how_to_apply": "Enroll through your bank branch, net banking, or contact your bank for the application form.",
        "official_link": "https://jansuraksha.gov.in",
        "potential_benefit_amount": "₹2,00,000 life cover"
    },
    {
        "id": "pmsby",
        "name": "PM Suraksha Bima Yojana",
        "short_name": "PMSBY",
        "category": "Health",
        "icon": "🚑",
        "description": "Accident insurance cover of ₹2 lakh for accidental death and ₹1 lakh for partial disability at just ₹20/year.",
        "benefits": "₹2,00,000 accidental death cover & ₹1,00,000 partial disability cover at ₹20/year",
        "eligibility": {
            "min_age": 18,
            "max_age": 70,
            "has_bank_account": True,
            "gender": "all",
            "categories": ["general", "obc", "sc", "st"]
        },
        "documents": ["Aadhaar Card", "Bank Account"],
        "how_to_apply": "Apply through your savings bank account. Forms available at all banks.",
        "official_link": "https://jansuraksha.gov.in",
        "potential_benefit_amount": "₹2,00,000 accident cover"
    },

    # ─────────────────── HOUSING ───────────────────
    {
        "id": "pm-awas",
        "name": "PM Awas Yojana",
        "short_name": "PMAY",
        "category": "Housing",
        "icon": "🏠",
        "description": "Housing subsidy for economically weaker sections, low and middle income groups to build or buy an affordable house.",
        "benefits": "Subsidy of ₹1.5 lakh to ₹2.67 lakh on home loan interest rates. Up to ₹1.20 lakh for house construction in rural areas.",
        "eligibility": {
            "max_income": 600000,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all",
            "min_age": 21
        },
        "documents": ["Aadhaar Card", "Income Proof", "Property Documents", "Bank Account"],
        "how_to_apply": "Apply online at pmaymis.gov.in or visit nearest CSC center. For rural areas, apply through Gram Panchayat.",
        "official_link": "https://pmaymis.gov.in",
        "potential_benefit_amount": "Up to ₹2,67,000 subsidy"
    },

    # ─────────────────── WOMEN & CHILD ───────────────────
    {
        "id": "sukanya-samriddhi",
        "name": "Sukanya Samriddhi Yojana",
        "short_name": "SSY",
        "category": "Women & Child",
        "icon": "👧",
        "description": "Government-backed savings scheme for the girl child with high interest rate (8.2%) and tax benefits under 80C. Matures when girl turns 21.",
        "benefits": "8.2% interest rate (highest among small savings), Tax-free returns, Partial withdrawal at age 18 for education",
        "eligibility": {
            "gender": "female",
            "max_age": 10,
            "categories": ["general", "obc", "sc", "st"]
        },
        "documents": ["Girl Child Birth Certificate", "Parent/Guardian Aadhaar & ID", "Address Proof"],
        "how_to_apply": "Open account at any post office or authorized bank with minimum ₹250 deposit.",
        "official_link": "https://www.india.gov.in/sukanya-samriddhi-yojana",
        "potential_benefit_amount": "8.2% annual interest + tax benefits"
    },
    {
        "id": "pm-matru-vandana",
        "name": "PM Matru Vandana Yojana",
        "short_name": "PMMVY",
        "category": "Women & Child",
        "icon": "🤰",
        "description": "Cash incentive of ₹11,000 for pregnant and lactating women for the first living child to improve health and nutrition.",
        "benefits": "₹11,000 in installments for first child (₹5,000 + ₹6,000 under Janani Suraksha Yojana)",
        "eligibility": {
            "gender": "female",
            "min_age": 19,
            "categories": ["general", "obc", "sc", "st"]
        },
        "documents": ["Aadhaar Card", "Bank Account", "MCP Card", "Pregnancy Registration"],
        "how_to_apply": "Register at nearest Anganwadi Centre or approved health facility. Apply through PMMVY portal.",
        "official_link": "https://pmmvy.wcd.gov.in",
        "potential_benefit_amount": "₹11,000"
    },
    {
        "id": "ujjwala",
        "name": "PM Ujjwala Yojana",
        "short_name": "PMUY",
        "category": "Women & Child",
        "icon": "🔥",
        "description": "Free LPG gas connection to women from BPL households to replace unhealthy cooking fuels like wood, coal, and dung cakes.",
        "benefits": "Free LPG connection + first refill free + stove provided. Subsidy on future refills.",
        "eligibility": {
            "gender": "female",
            "min_age": 18,
            "max_income": 200000,
            "categories": ["general", "obc", "sc", "st"]
        },
        "documents": ["Aadhaar Card", "BPL Ration Card", "Bank Account", "Passport Photo"],
        "how_to_apply": "Visit nearest LPG distributor (HP, Bharat, Indane) with required documents.",
        "official_link": "https://pmuy.gov.in",
        "potential_benefit_amount": "Free LPG connection worth ₹1,600+"
    },

    # ─────────────────── BUSINESS & EMPLOYMENT ───────────────────
    {
        "id": "mudra",
        "name": "PM Mudra Yojana",
        "short_name": "PMMY",
        "category": "Business",
        "icon": "💼",
        "description": "Collateral-free loans up to ₹10 lakh for small/micro businesses. Three categories: Shishu (up to ₹50K), Kishore (₹50K-5L), Tarun (₹5L-10L).",
        "benefits": "Collateral-free business loans: Shishu ₹50,000 | Kishore ₹5,00,000 | Tarun ₹10,00,000",
        "eligibility": {
            "min_age": 18,
            "occupations": ["business", "self-employed"],
            "gender": "all",
            "categories": ["general", "obc", "sc", "st"]
        },
        "documents": ["Aadhaar Card", "Business Plan/Proposal", "Identity & Address Proof", "Caste Certificate (if applicable)"],
        "how_to_apply": "Apply at any bank, NBFC, or MFI. Download forms from mudra.org.in.",
        "official_link": "https://www.mudra.org.in",
        "potential_benefit_amount": "Up to ₹10,00,000 loan"
    },
    {
        "id": "standup-india",
        "name": "Stand Up India",
        "short_name": "Stand Up India",
        "category": "Business",
        "icon": "🚀",
        "description": "Bank loans between ₹10 lakh and ₹1 crore for SC/ST and women entrepreneurs for setting up greenfield enterprises.",
        "benefits": "Loans ₹10 lakh to ₹1 crore for new business. Covers 75% of project cost. Repayment up to 7 years.",
        "eligibility": {
            "min_age": 18,
            "occupations": ["business", "self-employed", "unemployed"],
            "categories": ["sc", "st"],
            "gender": "all"
        },
        "documents": ["Aadhaar Card", "Caste Certificate", "Business Plan", "Address Proof", "IT Returns"],
        "how_to_apply": "Apply through standupmitra.in portal or visit any scheduled commercial bank.",
        "official_link": "https://www.standupmitra.in",
        "potential_benefit_amount": "₹10L to ₹1Cr loan"
    },
    {
        "id": "standup-india-women",
        "name": "Stand Up India (Women)",
        "short_name": "Stand Up India",
        "category": "Business",
        "icon": "👩‍💼",
        "description": "Bank loans between ₹10 lakh and ₹1 crore specifically for women entrepreneurs for setting up greenfield enterprises.",
        "benefits": "Loans ₹10 lakh to ₹1 crore for new business. Covers 75% of project cost. Repayment up to 7 years.",
        "eligibility": {
            "min_age": 18,
            "gender": "female",
            "occupations": ["business", "self-employed", "unemployed"],
            "categories": ["general", "obc", "sc", "st"]
        },
        "documents": ["Aadhaar Card", "Business Plan", "Address Proof", "IT Returns"],
        "how_to_apply": "Apply through standupmitra.in portal or visit any scheduled commercial bank.",
        "official_link": "https://www.standupmitra.in",
        "potential_benefit_amount": "₹10L to ₹1Cr loan"
    },
    {
        "id": "pm-vishwakarma",
        "name": "PM Vishwakarma Yojana",
        "short_name": "PM Vishwakarma",
        "category": "Business",
        "icon": "🔨",
        "description": "Support for traditional artisans and craftspeople with skill training, toolkit incentive, credit support, and digital marketing assistance.",
        "benefits": "₹15,000 toolkit incentive + Skill training + Loans up to ₹3 lakh at 5% interest + Digital marketing support",
        "eligibility": {
            "min_age": 18,
            "occupations": ["self-employed", "business"],
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Aadhaar Card", "Bank Account", "Trade-related documents"],
        "how_to_apply": "Register at pmvishwakarma.gov.in through CSC centers with Gram Panchayat/ULB verification.",
        "official_link": "https://pmvishwakarma.gov.in",
        "potential_benefit_amount": "₹15,000 + ₹3L loan"
    },
    {
        "id": "pm-svanidhi",
        "name": "PM SVANidhi",
        "short_name": "PM SVANidhi",
        "category": "Business",
        "icon": "🏪",
        "description": "Micro-credit facility for street vendors. Working capital loan up to ₹50,000 with 7% interest subsidy and digital payment rewards.",
        "benefits": "Loans: ₹10,000 (1st) → ₹20,000 (2nd) → ₹50,000 (3rd). 7% interest subsidy + ₹1,200/year cashback on digital payments.",
        "eligibility": {
            "min_age": 18,
            "occupations": ["business", "self-employed"],
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all",
            "max_income": 300000
        },
        "documents": ["Aadhaar Card", "Vending Certificate/Letter of Recommendation from ULB", "Bank Account"],
        "how_to_apply": "Apply online at pmsvanidhi.mohua.gov.in or through lending institutions.",
        "official_link": "https://pmsvanidhi.mohua.gov.in",
        "potential_benefit_amount": "Up to ₹50,000 loan"
    },
    {
        "id": "startup-india",
        "name": "Startup India",
        "short_name": "Startup India",
        "category": "Business",
        "icon": "💡",
        "description": "Recognition and support for startups including tax exemptions, easier compliance, IPR support, and access to government funding.",
        "benefits": "3-year tax holiday + Self-certification for 6 labor & 3 environmental laws + Fast-track patent filing + ₹10,000 Cr Fund of Funds access",
        "eligibility": {
            "min_age": 18,
            "occupations": ["business", "self-employed"],
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Business Registration Certificate", "PAN Card", "Aadhaar Card", "Innovation Description"],
        "how_to_apply": "Register at startupindia.gov.in. Get DPIIT recognition number.",
        "official_link": "https://www.startupindia.gov.in",
        "potential_benefit_amount": "Tax exemptions + funding access"
    },

    # ─────────────────── EDUCATION ───────────────────
    {
        "id": "national-scholarship",
        "name": "National Scholarship Portal (NSP)",
        "short_name": "NSP",
        "category": "Education",
        "icon": "🎓",
        "description": "One-stop platform for multiple central and state government scholarships for students from economically weaker backgrounds.",
        "benefits": "Scholarships ranging from ₹5,000 to ₹2,00,000/year depending on course and category",
        "eligibility": {
            "occupations": ["student"],
            "max_income": 800000,
            "categories": ["obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Aadhaar Card", "Income Certificate", "Caste Certificate", "Previous Marksheet", "Bank Account", "Institute Verification"],
        "how_to_apply": "Register at scholarships.gov.in. Apply during the scholarship window (usually Oct-Dec).",
        "official_link": "https://scholarships.gov.in",
        "potential_benefit_amount": "₹5,000 to ₹2,00,000/year"
    },
    {
        "id": "pm-kaushal",
        "name": "PM Kaushal Vikas Yojana",
        "short_name": "PMKVY",
        "category": "Education",
        "icon": "⚙️",
        "description": "Free skill development training and certification in 300+ job roles. Includes placement assistance and ₹8,000 reward on certification.",
        "benefits": "Free skill training + ₹8,000 reward on certification + Placement assistance + Industry-recognized certificate",
        "eligibility": {
            "min_age": 15,
            "max_age": 45,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all",
            "occupations": ["student", "unemployed", "salaried", "homemaker"]
        },
        "documents": ["Aadhaar Card", "Bank Account"],
        "how_to_apply": "Find nearest training center at pmkvyofficial.org. Enroll directly at the center.",
        "official_link": "https://www.pmkvyofficial.org",
        "potential_benefit_amount": "Free training + ₹8,000 reward"
    },
    {
        "id": "nap",
        "name": "National Apprenticeship Promotion Scheme",
        "short_name": "NAPS",
        "category": "Education",
        "icon": "🏭",
        "description": "Stipend support for apprentices in establishments. Government shares 25% of stipend (max ₹1,500/month) with employers.",
        "benefits": "Monthly stipend ₹5,000 to ₹9,000 depending on qualification + Hands-on training + Certificate",
        "eligibility": {
            "min_age": 14,
            "max_age": 30,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all",
            "occupations": ["student", "unemployed"]
        },
        "documents": ["Aadhaar Card", "Educational Certificates", "Bank Account"],
        "how_to_apply": "Register at apprenticeshipindia.gov.in. Search and apply for apprenticeship opportunities.",
        "official_link": "https://www.apprenticeshipindia.gov.in",
        "potential_benefit_amount": "₹5,000-₹9,000/month stipend"
    },

    # ─────────────────── FINANCIAL INCLUSION ───────────────────
    {
        "id": "jan-dhan",
        "name": "PM Jan Dhan Yojana",
        "short_name": "PMJDY",
        "category": "Financial Inclusion",
        "icon": "🏦",
        "description": "Zero-balance bank account with RuPay debit card, ₹2 lakh accident insurance, and ₹30,000 life cover. Overdraft facility up to ₹10,000.",
        "benefits": "Zero balance account + RuPay card + ₹2L accident insurance + ₹30,000 life cover + ₹10,000 overdraft",
        "eligibility": {
            "min_age": 10,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Aadhaar Card or any ID Proof", "Passport Photo"],
        "how_to_apply": "Visit nearest bank branch or Bank Mitra. No minimum balance required.",
        "official_link": "https://pmjdy.gov.in",
        "potential_benefit_amount": "₹2L insurance + ₹10K overdraft"
    },
    {
        "id": "atal-pension",
        "name": "Atal Pension Yojana",
        "short_name": "APY",
        "category": "Financial Inclusion",
        "icon": "👴",
        "description": "Guaranteed minimum pension of ₹1,000 to ₹5,000/month after age 60 for workers in the unorganized sector.",
        "benefits": "Guaranteed pension ₹1,000-₹5,000/month after 60. Government co-contributes 50% for eligible subscribers (up to 5 years).",
        "eligibility": {
            "min_age": 18,
            "max_age": 40,
            "has_bank_account": True,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all",
            "occupations": ["farmer", "self-employed", "business", "salaried", "unemployed", "homemaker"]
        },
        "documents": ["Aadhaar Card", "Bank Account", "Mobile Number"],
        "how_to_apply": "Apply through your bank or online via enps.nsdl.com. Auto-debit from savings account.",
        "official_link": "https://jansuraksha.gov.in",
        "potential_benefit_amount": "₹1,000-₹5,000/month pension"
    },

    # ─────────────────── ENERGY ───────────────────
    {
        "id": "pm-surya-ghar",
        "name": "PM Surya Ghar: Muft Bijli Yojana",
        "short_name": "PM Surya Ghar",
        "category": "Energy",
        "icon": "☀️",
        "description": "Subsidy for installing rooftop solar panels. Get up to 300 units of free electricity every month and earn from surplus power.",
        "benefits": "Up to ₹78,000 subsidy for solar installation. 300 units free electricity/month. Earn by selling surplus to grid.",
        "eligibility": {
            "min_age": 18,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Aadhaar Card", "Electricity Bill", "Bank Account", "Property Documents"],
        "how_to_apply": "Register at pmsuryaghar.gov.in. Apply through your electricity distribution company.",
        "official_link": "https://pmsuryaghar.gov.in",
        "potential_benefit_amount": "₹78,000 subsidy + free electricity"
    },

    # ─────────────────── FOOD SECURITY ───────────────────
    {
        "id": "pm-garib-kalyan",
        "name": "PM Garib Kalyan Anna Yojana",
        "short_name": "PMGKAY",
        "category": "Food Security",
        "icon": "🍚",
        "description": "Free food grains (5 kg/person/month) to over 80 crore beneficiaries under the National Food Security Act.",
        "benefits": "5 kg free food grains per person per month (rice, wheat, coarse grains)",
        "eligibility": {
            "categories": ["general", "obc", "sc", "st"],
            "max_income": 200000,
            "gender": "all"
        },
        "documents": ["Ration Card (Priority Household/Antyodaya)", "Aadhaar Card"],
        "how_to_apply": "Get ration card from State Food & Civil Supplies Department. Collect grains from nearest Fair Price Shop.",
        "official_link": "https://nfsa.gov.in",
        "potential_benefit_amount": "Free food grains monthly"
    },
    {
        "id": "mgnrega",
        "name": "MGNREGA",
        "short_name": "MGNREGA",
        "category": "Employment",
        "icon": "👷",
        "description": "Guarantees 100 days of wage employment per year to every rural household whose adult members volunteer for unskilled manual work.",
        "benefits": "100 days guaranteed employment/year at ₹267-₹374/day (varies by state). Unemployment allowance if work not provided within 15 days.",
        "eligibility": {
            "min_age": 18,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all",
            "occupations": ["farmer", "unemployed", "self-employed", "homemaker"]
        },
        "documents": ["Job Card (apply at Gram Panchayat)", "Aadhaar Card", "Bank/Post Office Account"],
        "how_to_apply": "Apply for Job Card at Gram Panchayat. Demand work in writing. Work must be provided within 15 days.",
        "official_link": "https://nrega.nic.in",
        "potential_benefit_amount": "₹267-₹374/day for 100 days"
    },

    # ─────────────────── SENIOR CITIZENS ───────────────────
    {
        "id": "indira-gandhi-pension",
        "name": "Indira Gandhi National Old Age Pension",
        "short_name": "IGNOAPS",
        "category": "Senior Citizens",
        "icon": "🧓",
        "description": "Monthly pension of ₹200-₹500 for senior citizens from BPL families. States often add their own top-up amount.",
        "benefits": "₹200/month (60-79 years) or ₹500/month (80+ years) from Centre. States add ₹200-₹1,500 more.",
        "eligibility": {
            "min_age": 60,
            "max_income": 200000,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Age Proof", "BPL Certificate", "Aadhaar Card", "Bank Account"],
        "how_to_apply": "Apply through District Social Welfare Office or Gram Panchayat/Municipal Office.",
        "official_link": "https://nsap.nic.in",
        "potential_benefit_amount": "₹200-₹2,000/month"
    },
]


# Indian states list for the form dropdown
INDIAN_STATES = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal",
    "Andaman & Nicobar Islands", "Chandigarh", "Dadra & Nagar Haveli and Daman & Diu",
    "Delhi", "Jammu & Kashmir", "Ladakh", "Lakshadweep", "Puducherry"
]
