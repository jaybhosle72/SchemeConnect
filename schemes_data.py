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

    # ─────────────────── ADDITIONAL AGRICULTURE ───────────────────
    {
        "id": "fasal-bima",
        "name": "PM Fasal Bima Yojana",
        "short_name": "PMFBY",
        "category": "Agriculture",
        "icon": "🌿",
        "description": "Crop insurance scheme providing financial support to farmers in case of crop failure due to natural calamities, pests, and diseases.",
        "benefits": "Low premium: 2% for Kharif, 1.5% for Rabi, 5% for commercial crops. Full sum insured for crop loss.",
        "eligibility": {
            "occupations": ["farmer"],
            "has_land": True,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Aadhaar Card", "Land Records", "Bank Account", "Sowing Certificate"],
        "how_to_apply": "Apply through bank, CSC, or pmfby.gov.in before sowing season deadline.",
        "official_link": "https://pmfby.gov.in",
        "potential_benefit_amount": "Full crop value insurance"
    },
    {
        "id": "kisan-credit",
        "name": "Kisan Credit Card",
        "short_name": "KCC",
        "category": "Agriculture",
        "icon": "💳",
        "description": "Flexible credit facility for farmers to meet their agricultural and allied expenses including crop cultivation and farm maintenance.",
        "benefits": "Credit up to ₹3 lakh at 4% interest (after subsidy). Crop insurance included. Flexible repayment.",
        "eligibility": {
            "occupations": ["farmer"],
            "min_age": 18,
            "max_age": 75,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Aadhaar Card", "Land Records", "Passport Photo", "Bank Account"],
        "how_to_apply": "Apply at any bank branch or through PM-KISAN portal for existing PM-KISAN beneficiaries.",
        "official_link": "https://pmkisan.gov.in",
        "potential_benefit_amount": "Up to ₹3,00,000 credit at 4%"
    },
    {
        "id": "soil-health",
        "name": "Soil Health Card Scheme",
        "short_name": "SHC",
        "category": "Agriculture",
        "icon": "🧪",
        "description": "Free soil testing and health card for farmers with crop-wise fertilizer recommendations to improve productivity and reduce costs.",
        "benefits": "Free soil testing every 2 years. Customized fertilizer recommendations. Improved crop yield by 10-15%.",
        "eligibility": {
            "occupations": ["farmer"],
            "has_land": True,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Aadhaar Card", "Land Details"],
        "how_to_apply": "Contact nearest Krishi Vigyan Kendra or Agriculture Department. Apply at soilhealth.dac.gov.in.",
        "official_link": "https://soilhealth.dac.gov.in",
        "potential_benefit_amount": "Free soil testing + higher yield"
    },

    # ─────────────────── ADDITIONAL HEALTH ───────────────────
    {
        "id": "janani-suraksha",
        "name": "Janani Suraksha Yojana",
        "short_name": "JSY",
        "category": "Health",
        "icon": "🏥",
        "description": "Cash assistance to pregnant women for institutional delivery to reduce maternal and neonatal mortality.",
        "benefits": "₹1,400 (rural) or ₹1,000 (urban) cash assistance for hospital delivery. Free delivery services.",
        "eligibility": {
            "gender": "female",
            "min_age": 19,
            "max_income": 300000,
            "categories": ["general", "obc", "sc", "st"]
        },
        "documents": ["Aadhaar Card", "JSY Card", "Bank Account", "Delivery Certificate"],
        "how_to_apply": "Register at nearest government hospital or Anganwadi center during pregnancy.",
        "official_link": "https://nhm.gov.in",
        "potential_benefit_amount": "₹1,000-₹1,400 per delivery"
    },
    {
        "id": "ab-health-wellness",
        "name": "Ayushman Bharat Health & Wellness Centers",
        "short_name": "AB-HWC",
        "category": "Health",
        "icon": "⚕️",
        "description": "Free primary healthcare services including free essential medicines, diagnostics, and teleconsultation at 1.5 lakh Health & Wellness Centers.",
        "benefits": "Free OPD consultation, 12 types of free diagnostics, free essential medicines, teleconsultation, yoga & wellness activities.",
        "eligibility": {
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Aadhaar Card or any ID Proof"],
        "how_to_apply": "Visit nearest Health & Wellness Center (erstwhile Sub Centre/PHC). No registration needed.",
        "official_link": "https://ab-hwc.nhp.gov.in",
        "potential_benefit_amount": "Free healthcare services"
    },

    # ─────────────────── ADDITIONAL EDUCATION ───────────────────
    {
        "id": "central-scholarship-sc",
        "name": "Post Matric Scholarship for SC Students",
        "short_name": "PMS-SC",
        "category": "Education",
        "icon": "📚",
        "description": "Full scholarship for SC students studying post-matric (Class 11 onwards) covering tuition fees, maintenance allowance, and study tour charges.",
        "benefits": "Full tuition fee + ₹550-₹1,200/month maintenance + Book allowance + Study tour charges",
        "eligibility": {
            "categories": ["sc"],
            "occupations": ["student"],
            "max_income": 250000,
            "gender": "all"
        },
        "documents": ["Caste Certificate", "Income Certificate", "Marksheets", "Aadhaar Card", "Bank Account"],
        "how_to_apply": "Apply through National Scholarship Portal (scholarships.gov.in) during Oct-Dec window.",
        "official_link": "https://scholarships.gov.in",
        "potential_benefit_amount": "Full tuition + ₹14,400/year"
    },
    {
        "id": "central-scholarship-st",
        "name": "Post Matric Scholarship for ST Students",
        "short_name": "PMS-ST",
        "category": "Education",
        "icon": "📖",
        "description": "Scholarship for ST students studying post-matric covering full tuition fees, maintenance allowance, and additional allowances.",
        "benefits": "Full tuition + ₹550-₹1,200/month maintenance + Book grant + Thesis typing charges",
        "eligibility": {
            "categories": ["st"],
            "occupations": ["student"],
            "max_income": 250000,
            "gender": "all"
        },
        "documents": ["Tribe Certificate", "Income Certificate", "Marksheets", "Aadhaar Card", "Bank Account"],
        "how_to_apply": "Apply through National Scholarship Portal (scholarships.gov.in).",
        "official_link": "https://scholarships.gov.in",
        "potential_benefit_amount": "Full tuition + ₹14,400/year"
    },
    {
        "id": "obc-scholarship",
        "name": "Post Matric Scholarship for OBC Students",
        "short_name": "PMS-OBC",
        "category": "Education",
        "icon": "🎓",
        "description": "Financial assistance for OBC students studying in post-matric or post-secondary courses in recognized institutions.",
        "benefits": "Tuition fee reimbursement + ₹500-₹1,000/month maintenance allowance",
        "eligibility": {
            "categories": ["obc"],
            "occupations": ["student"],
            "max_income": 300000,
            "gender": "all"
        },
        "documents": ["OBC Certificate", "Income Certificate", "Marksheets", "Aadhaar Card", "Bank Account"],
        "how_to_apply": "Apply through National Scholarship Portal (scholarships.gov.in).",
        "official_link": "https://scholarships.gov.in",
        "potential_benefit_amount": "Tuition + ₹12,000/year"
    },
    {
        "id": "vidyalakshmi",
        "name": "Vidya Lakshmi Education Loan Portal",
        "short_name": "Vidya Lakshmi",
        "category": "Education",
        "icon": "🏫",
        "description": "Single window portal for students to access education loans from multiple banks and apply for government scholarships.",
        "benefits": "Education loans up to ₹20 lakh (India) / ₹30 lakh (abroad). Interest subsidy for economically weaker students.",
        "eligibility": {
            "occupations": ["student"],
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all",
            "min_age": 16,
            "max_age": 35
        },
        "documents": ["Admission Letter", "Course Fee Structure", "Marksheets", "Aadhaar Card", "Income Proof"],
        "how_to_apply": "Register at vidyalakshmi.co.in. Apply to multiple banks through single form.",
        "official_link": "https://www.vidyalakshmi.co.in",
        "potential_benefit_amount": "Up to ₹20L education loan"
    },
    {
        "id": "free-coaching-sc",
        "name": "Free Coaching for SC/ST Students",
        "short_name": "Free Coaching",
        "category": "Education",
        "icon": "✏️",
        "description": "Free coaching for competitive exams (UPSC, SSC, Banking, Engineering, Medical) for SC/ST students at reputed coaching institutes.",
        "benefits": "Free coaching at top institutes + ₹3,000/month stipend + ₹15,000/year book allowance",
        "eligibility": {
            "categories": ["sc", "st"],
            "occupations": ["student", "unemployed"],
            "max_income": 600000,
            "gender": "all",
            "min_age": 16,
            "max_age": 35
        },
        "documents": ["Caste Certificate", "Income Certificate", "Educational Certificates", "Aadhaar Card"],
        "how_to_apply": "Apply through coaching.dosje.gov.in when applications are open (usually July-Sept).",
        "official_link": "https://coaching.dosje.gov.in",
        "potential_benefit_amount": "Free coaching + ₹51,000/year"
    },

    # ─────────────────── WOMEN EMPOWERMENT ───────────────────
    {
        "id": "mahila-samman",
        "name": "Mahila Samman Savings Certificate",
        "short_name": "MSSC",
        "category": "Women & Child",
        "icon": "💰",
        "description": "Special savings scheme for women offering 7.5% interest rate with partial withdrawal facility. Invest up to ₹2 lakh for 2 years.",
        "benefits": "7.5% annual interest (highest among fixed deposits). Partial withdrawal after 1 year. Tax benefits.",
        "eligibility": {
            "gender": "female",
            "categories": ["general", "obc", "sc", "st"]
        },
        "documents": ["Aadhaar Card", "PAN Card", "Bank Account"],
        "how_to_apply": "Open at any post office or authorized bank. Minimum deposit ₹1,000.",
        "official_link": "https://www.indiapost.gov.in",
        "potential_benefit_amount": "7.5% interest on up to ₹2L"
    },
    {
        "id": "free-silai-machine",
        "name": "Free Silai Machine Yojana",
        "short_name": "Silai Machine",
        "category": "Women & Child",
        "icon": "🧵",
        "description": "Free sewing machine distribution to poor and labor class women to enable self-employment and financial independence.",
        "benefits": "Free sewing machine + Basic training for tailoring and stitching",
        "eligibility": {
            "gender": "female",
            "min_age": 20,
            "max_age": 40,
            "max_income": 200000,
            "categories": ["general", "obc", "sc", "st"]
        },
        "documents": ["Aadhaar Card", "Income Certificate", "Age Proof", "Passport Photo", "Mobile Number"],
        "how_to_apply": "Apply through India.gov.in or contact District Industries Center.",
        "official_link": "https://www.india.gov.in",
        "potential_benefit_amount": "Free sewing machine"
    },
    {
        "id": "one-stop-centre",
        "name": "One Stop Centre (Sakhi)",
        "short_name": "OSC",
        "category": "Women & Child",
        "icon": "🛡️",
        "description": "Support center for women affected by violence providing medical aid, legal aid, counseling, shelter, and police facilitation under one roof.",
        "benefits": "Free medical aid + Legal assistance + Psychological counseling + Temporary shelter (up to 5 days) + Police facilitation",
        "eligibility": {
            "gender": "female",
            "categories": ["general", "obc", "sc", "st"]
        },
        "documents": ["No documents required for emergency support"],
        "how_to_apply": "Call Women Helpline 181 or visit nearest One Stop Centre. Can also reach through Sakhi app.",
        "official_link": "https://wcd.nic.in",
        "potential_benefit_amount": "Free support services"
    },
    {
        "id": "beti-bachao",
        "name": "Beti Bachao Beti Padhao",
        "short_name": "BBBP",
        "category": "Women & Child",
        "icon": "👧",
        "description": "National campaign for survival, protection, and education of the girl child. Promotes girl child education with financial incentives.",
        "benefits": "Awareness campaigns + Girl child education support + Sukanya Samriddhi account linkage + Community mobilization",
        "eligibility": {
            "gender": "female",
            "max_age": 18,
            "categories": ["general", "obc", "sc", "st"]
        },
        "documents": ["Birth Certificate", "Aadhaar Card", "School Certificate"],
        "how_to_apply": "Contact District Women & Child Development Office or nearest Anganwadi center.",
        "official_link": "https://wcd.nic.in/bbbp-schemes",
        "potential_benefit_amount": "Education support + awareness"
    },

    # ─────────────────── DISABILITY ───────────────────
    {
        "id": "disability-pension",
        "name": "Indira Gandhi National Disability Pension",
        "short_name": "IGNDPS",
        "category": "Disability",
        "icon": "♿",
        "description": "Monthly pension for persons with severe and multiple disabilities (80%+) belonging to BPL households.",
        "benefits": "₹300/month from Centre (18-79 years) or ₹500/month (80+ years). States add additional amount.",
        "eligibility": {
            "min_age": 18,
            "max_income": 200000,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Disability Certificate (80%+)", "BPL Certificate", "Aadhaar Card", "Bank Account"],
        "how_to_apply": "Apply through District Social Welfare Office or Gram Panchayat.",
        "official_link": "https://nsap.nic.in",
        "potential_benefit_amount": "₹300-₹500/month pension"
    },
    {
        "id": "adip",
        "name": "Assistance for Disabled Persons (ADIP)",
        "short_name": "ADIP",
        "category": "Disability",
        "icon": "🦽",
        "description": "Free assistive devices and aids like wheelchairs, hearing aids, artificial limbs, and Braille kits for persons with disabilities.",
        "benefits": "Free modern aids & appliances worth up to ₹10,000. Travel expense reimbursement for fitting camps.",
        "eligibility": {
            "max_income": 300000,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Disability Certificate (40%+)", "Income Certificate", "Aadhaar Card", "Prescription from Doctor"],
        "how_to_apply": "Apply through ALIMCO (alimco.in) or attend assistance camps organized by implementing agencies.",
        "official_link": "https://www.alimco.in",
        "potential_benefit_amount": "Free aids worth ₹10,000+"
    },
    {
        "id": "sugamya-bharat",
        "name": "Accessible India Campaign (Sugamya Bharat)",
        "short_name": "Sugamya Bharat",
        "category": "Disability",
        "icon": "🏗️",
        "description": "Making public spaces, transport, and ICT accessible for persons with disabilities. Includes accessible websites, buildings, and transport.",
        "benefits": "Accessible government buildings, websites, and transport. Sign language interpreters. Accessible formats of documents.",
        "eligibility": {
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Disability Certificate"],
        "how_to_apply": "Report accessibility issues at accessibleindia.gov.in or through Sugamya Bharat app.",
        "official_link": "https://accessibleindia.gov.in",
        "potential_benefit_amount": "Improved accessibility"
    },

    # ─────────────────── LABOUR & WORKERS ───────────────────
    {
        "id": "epfo",
        "name": "Employee Provident Fund (EPF)",
        "short_name": "EPF",
        "category": "Labour",
        "icon": "🏢",
        "description": "Mandatory savings scheme for salaried employees earning up to ₹15,000/month. Employer contributes equal amount. 8.25% annual interest.",
        "benefits": "12% employee + 12% employer contribution. 8.25% tax-free interest. Pension after 58. Life insurance up to ₹7 lakh.",
        "eligibility": {
            "occupations": ["salaried"],
            "min_age": 18,
            "max_age": 58,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Aadhaar Card", "PAN Card", "Bank Account", "Employment Letter"],
        "how_to_apply": "Automatic enrollment by employer for organizations with 20+ employees. Check balance at epfindia.gov.in.",
        "official_link": "https://www.epfindia.gov.in",
        "potential_benefit_amount": "Retirement corpus + pension"
    },
    {
        "id": "esic",
        "name": "Employee State Insurance (ESI)",
        "short_name": "ESIC",
        "category": "Labour",
        "icon": "🩺",
        "description": "Social security and health insurance for workers earning up to ₹21,000/month. Covers medical, sickness, maternity, and disability benefits.",
        "benefits": "Free medical care for family. 70% salary during sickness. 100% salary during maternity (26 weeks). Disability pension.",
        "eligibility": {
            "occupations": ["salaried"],
            "max_income": 252000,
            "min_age": 18,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Aadhaar Card", "Employment Details", "Bank Account", "Family Photo"],
        "how_to_apply": "Automatic enrollment by employer. Get ESI card from nearest ESIC branch office.",
        "official_link": "https://www.esic.gov.in",
        "potential_benefit_amount": "Free healthcare + salary during leave"
    },
    {
        "id": "e-shram",
        "name": "e-Shram Card (Unorganized Workers)",
        "short_name": "e-Shram",
        "category": "Labour",
        "icon": "👷",
        "description": "National database for unorganized workers providing unique ID and access to social security schemes. Includes accidental insurance of ₹2 lakh.",
        "benefits": "₹2 lakh accidental insurance (free). Access to PM schemes. Digital identity for welfare benefits.",
        "eligibility": {
            "min_age": 16,
            "max_age": 59,
            "max_income": 200000,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all",
            "occupations": ["farmer", "self-employed", "business", "unemployed", "homemaker"]
        },
        "documents": ["Aadhaar Card", "Bank Account", "Mobile Number"],
        "how_to_apply": "Register at eshram.gov.in or through nearest CSC center. Self-registration with Aadhaar and mobile.",
        "official_link": "https://eshram.gov.in",
        "potential_benefit_amount": "₹2L insurance + scheme access"
    },
    {
        "id": "pm-shram-yogi",
        "name": "PM Shram Yogi MaanDhan Yojana",
        "short_name": "PM-SYM",
        "category": "Labour",
        "icon": "🔧",
        "description": "Voluntary pension scheme for unorganized workers. Contribute ₹55-₹200/month based on age and get ₹3,000/month pension after 60.",
        "benefits": "₹3,000/month guaranteed pension after age 60. Government matches your contribution. Family pension for spouse.",
        "eligibility": {
            "min_age": 18,
            "max_age": 40,
            "max_income": 180000,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all",
            "occupations": ["farmer", "self-employed", "business", "homemaker"]
        },
        "documents": ["Aadhaar Card", "Bank Account", "Mobile Number"],
        "how_to_apply": "Register through CSC center or at maandhan.in. Monthly auto-debit from bank account.",
        "official_link": "https://maandhan.in",
        "potential_benefit_amount": "₹3,000/month pension after 60"
    },

    # ─────────────────── DIGITAL & TECHNOLOGY ───────────────────
    {
        "id": "digital-india",
        "name": "Digital India - Free Wi-Fi (PM WANI)",
        "short_name": "PM WANI",
        "category": "Digital",
        "icon": "📶",
        "description": "Free or affordable public Wi-Fi hotspots across India through PM WANI (Wi-Fi Access Network Interface) scheme.",
        "benefits": "Free Wi-Fi access at public places. Affordable broadband connectivity. Business opportunity as Wi-Fi provider.",
        "eligibility": {
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Mobile Number for OTP verification"],
        "how_to_apply": "Connect to PM WANI hotspot in your area. Verify with mobile OTP. Start browsing.",
        "official_link": "https://dot.gov.in/pm-wani",
        "potential_benefit_amount": "Free Wi-Fi access"
    },
    {
        "id": "digilocker",
        "name": "DigiLocker",
        "short_name": "DigiLocker",
        "category": "Digital",
        "icon": "📱",
        "description": "Free cloud-based platform to store, share, and verify documents digitally. Accepted as valid documents by government agencies.",
        "benefits": "Free digital document storage. Verified certificates from universities/boards. Paperless governance. Valid for all government services.",
        "eligibility": {
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Aadhaar Card for registration"],
        "how_to_apply": "Download DigiLocker app or register at digilocker.gov.in with Aadhaar.",
        "official_link": "https://www.digilocker.gov.in",
        "potential_benefit_amount": "Free digital document storage"
    },

    # ─────────────────── ADDITIONAL SENIOR CITIZENS ───────────────────
    {
        "id": "senior-citizen-savings",
        "name": "Senior Citizens Savings Scheme",
        "short_name": "SCSS",
        "category": "Senior Citizens",
        "icon": "🏦",
        "description": "Government-backed savings scheme for senior citizens (60+) offering 8.2% interest with quarterly payouts and tax benefits.",
        "benefits": "8.2% annual interest paid quarterly. Maximum deposit ₹30 lakh. Tax benefit under 80C. Premature withdrawal allowed.",
        "eligibility": {
            "min_age": 60,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Age Proof", "Aadhaar Card", "PAN Card", "Passport Photo"],
        "how_to_apply": "Open account at any post office or authorized bank. Minimum deposit ₹1,000.",
        "official_link": "https://www.indiapost.gov.in",
        "potential_benefit_amount": "8.2% interest on up to ₹30L"
    },
    {
        "id": "vayoshreshtha",
        "name": "Rashtriya Vayoshri Yojana",
        "short_name": "RVY",
        "category": "Senior Citizens",
        "icon": "🧓",
        "description": "Free physical aids and assisted living devices for senior citizens belonging to BPL category to improve their quality of life.",
        "benefits": "Free walking sticks, spectacles, hearing aids, dentures, wheelchairs, and other assisted devices.",
        "eligibility": {
            "min_age": 60,
            "max_income": 200000,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Age Proof", "BPL Certificate", "Aadhaar Card"],
        "how_to_apply": "Attend free distribution camps organized by ALIMCO in your district. Contact District Social Welfare Officer.",
        "official_link": "https://www.alimco.in",
        "potential_benefit_amount": "Free assisted devices"
    },

    # ─────────────────── RURAL DEVELOPMENT ───────────────────
    {
        "id": "pm-gram-sadak",
        "name": "PM Gram Sadak Yojana",
        "short_name": "PMGSY",
        "category": "Rural",
        "icon": "🛣️",
        "description": "All-weather road connectivity to unconnected rural habitations. Includes road construction, upgradation, and maintenance.",
        "benefits": "All-weather road to your village. Better market access. Improved healthcare & education access. Employment during construction.",
        "eligibility": {
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["No individual application needed — implemented through Gram Panchayat"],
        "how_to_apply": "Contact Gram Panchayat or District Rural Development Agency. Check status at omms.nic.in.",
        "official_link": "https://omms.nic.in",
        "potential_benefit_amount": "Road connectivity to village"
    },
    {
        "id": "swachh-bharat-gramin",
        "name": "Swachh Bharat Mission (Gramin)",
        "short_name": "SBM-G",
        "category": "Rural",
        "icon": "🚽",
        "description": "Financial incentive for construction of individual household toilets in rural areas to achieve open defecation free status.",
        "benefits": "₹12,000 incentive for toilet construction. Free solid & liquid waste management. Village-level sanitation infrastructure.",
        "eligibility": {
            "max_income": 300000,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Aadhaar Card", "BPL Card/Income Proof", "Bank Account", "Photo of household"],
        "how_to_apply": "Apply through Gram Panchayat or Block Development Office. Register at sbm.gov.in.",
        "official_link": "https://sbm.gov.in",
        "potential_benefit_amount": "₹12,000 for toilet construction"
    },
    {
        "id": "pm-awas-gramin",
        "name": "PM Awas Yojana - Gramin",
        "short_name": "PMAY-G",
        "category": "Housing",
        "icon": "🏡",
        "description": "Financial assistance for construction of pucca house with basic amenities for rural homeless and those living in kutcha/dilapidated houses.",
        "benefits": "₹1,20,000 (plain areas) or ₹1,30,000 (hilly areas) for house construction + 90/95 days MGNREGA wages.",
        "eligibility": {
            "max_income": 200000,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all",
            "min_age": 18
        },
        "documents": ["Aadhaar Card", "Job Card", "Bank Account", "SECC Data verification"],
        "how_to_apply": "Selected from SECC-2011 data. Contact Gram Panchayat or Block Development Office.",
        "official_link": "https://pmayg.nic.in",
        "potential_benefit_amount": "₹1,20,000-₹1,30,000"
    },

    # ─────────────────── ADDITIONAL FINANCIAL ───────────────────
    {
        "id": "national-pension",
        "name": "National Pension System (NPS)",
        "short_name": "NPS",
        "category": "Financial Inclusion",
        "icon": "📊",
        "description": "Voluntary retirement savings scheme with market-linked returns. Extra tax benefit of ₹50,000 under Section 80CCD(1B) over and above 80C limit.",
        "benefits": "Market-linked returns (10-12% average). Extra ₹50,000 tax deduction. 60% lump sum at retirement. 40% as annuity pension.",
        "eligibility": {
            "min_age": 18,
            "max_age": 70,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all",
            "has_bank_account": True
        },
        "documents": ["Aadhaar Card", "PAN Card", "Bank Account", "Passport Photo"],
        "how_to_apply": "Open account at enps.nsdl.com or through any POP (Point of Presence) like banks and post offices.",
        "official_link": "https://npscra.nsdl.co.in",
        "potential_benefit_amount": "Retirement corpus + tax savings"
    },
    {
        "id": "pmjjy-micro-pension",
        "name": "PM Kisan MaanDhan Yojana",
        "short_name": "PM-KMY",
        "category": "Agriculture",
        "icon": "👨‍🌾",
        "description": "Pension scheme for small and marginal farmers. Contribute ₹55-₹200/month and get ₹3,000/month guaranteed pension after age 60.",
        "benefits": "₹3,000/month pension after age 60. Government matches equal contribution. Family pension for spouse after death.",
        "eligibility": {
            "min_age": 18,
            "max_age": 40,
            "occupations": ["farmer"],
            "has_land": True,
            "categories": ["general", "obc", "sc", "st"],
            "gender": "all"
        },
        "documents": ["Aadhaar Card", "Bank Account", "Land Records"],
        "how_to_apply": "Register through nearest CSC center or at maandhan.in with Aadhaar and bank details.",
        "official_link": "https://maandhan.in/shramyogi",
        "potential_benefit_amount": "₹3,000/month pension after 60"
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
