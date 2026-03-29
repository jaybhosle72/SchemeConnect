/**
 * SchemeConnect AI — Frontend Application Logic
 * Google Solution Challenge 2026
 * 
 * Handles: Multi-step form, API calls, results rendering, AI chat
 */

// ─────────── STATE ───────────
let currentStep = 1;
const totalSteps = 3;
let matchedSchemes = [];
let chatOpen = false;

// ─────────── INITIALIZATION ───────────
document.addEventListener('DOMContentLoaded', () => {
    loadStates();
    initNavScroll();
    initForm();
    initIncomeHints();
    initChatInput();
});


// ─────────── LOAD STATES DROPDOWN ───────────
async function loadStates() {
    const stateSelect = document.getElementById('state');
    try {
        const res = await fetch('/api/states');
        const data = await res.json();
        data.states.forEach(state => {
            const opt = document.createElement('option');
            opt.value = state;
            opt.textContent = state;
            stateSelect.appendChild(opt);
        });
    } catch (e) {
        // Fallback: hardcoded states
        const states = [
            "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
            "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
            "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
            "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
            "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
            "Uttar Pradesh", "Uttarakhand", "West Bengal"
        ];
        states.forEach(state => {
            const opt = document.createElement('option');
            opt.value = state;
            opt.textContent = state;
            stateSelect.appendChild(opt);
        });
    }
}


// ─────────── NAVBAR SCROLL EFFECT ───────────
function initNavScroll() {
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
}


// ─────────── SMOOTH SCROLL ───────────
function scrollToSection(sectionId) {
    const el = document.getElementById(sectionId);
    if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
}


// ─────────── MULTI-STEP FORM ───────────
function initForm() {
    const form = document.getElementById('scheme-form');
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        submitForm();
    });
}

function nextStep(step) {
    // Validate current step
    if (!validateStep(currentStep)) return;

    // Update UI
    document.getElementById(`step-${currentStep}`).classList.remove('active');
    document.getElementById(`step-${step}`).classList.add('active');

    // Update progress
    currentStep = step;
    updateProgress();
}

function prevStep(step) {
    document.getElementById(`step-${currentStep}`).classList.remove('active');
    document.getElementById(`step-${step}`).classList.add('active');
    currentStep = step;
    updateProgress();
}

function updateProgress() {
    // Update progress bar fill
    const fill = document.getElementById('progress-fill');
    fill.style.width = `${(currentStep / totalSteps) * 100}%`;

    // Update step indicators
    document.querySelectorAll('.progress-step').forEach((el, i) => {
        const stepNum = i + 1;
        el.classList.remove('active', 'done');
        if (stepNum === currentStep) {
            el.classList.add('active');
        } else if (stepNum < currentStep) {
            el.classList.add('done');
        }
    });
}

function validateStep(step) {
    const stepEl = document.getElementById(`step-${step}`);
    const inputs = stepEl.querySelectorAll('input[required], select[required]');
    let valid = true;

    inputs.forEach(input => {
        if (input.type === 'radio') {
            // Check if any radio in the group is checked
            const name = input.name;
            const checked = stepEl.querySelector(`input[name="${name}"]:checked`);
            if (!checked) {
                valid = false;
                highlightRadioGroup(input.name);
            }
        } else if (!input.value.trim()) {
            valid = false;
            input.style.borderColor = 'var(--accent-rose)';
            input.style.boxShadow = '0 0 0 3px rgba(244, 63, 94, 0.15)';
            setTimeout(() => {
                input.style.borderColor = '';
                input.style.boxShadow = '';
            }, 2000);
        }
    });

    if (!valid) {
        // Subtle shake animation
        stepEl.style.animation = 'none';
        stepEl.offsetHeight; // trigger reflow
        stepEl.style.animation = 'shake 0.4s ease-out';
    }

    return valid;
}

function highlightRadioGroup(name) {
    const labels = document.querySelectorAll(`input[name="${name}"] + .radio-label, input[name="${name}"] + .toggle-label`);
    labels.forEach(label => {
        label.style.borderColor = 'var(--accent-rose)';
        setTimeout(() => {
            label.style.borderColor = '';
        }, 2000);
    });
}

// Add shake animation dynamically
const shakeStyle = document.createElement('style');
shakeStyle.textContent = `
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        20% { transform: translateX(-8px); }
        40% { transform: translateX(8px); }
        60% { transform: translateX(-4px); }
        80% { transform: translateX(4px); }
    }
`;
document.head.appendChild(shakeStyle);


// ─────────── INCOME HINTS ───────────
function initIncomeHints() {
    const incomeInput = document.getElementById('income');
    const incomeHint = document.getElementById('income-hint');

    incomeInput.addEventListener('input', () => {
        const val = parseInt(incomeInput.value);
        if (isNaN(val)) {
            incomeHint.textContent = 'Enter approximate yearly income';
            return;
        }

        if (val < 100000) {
            incomeHint.textContent = `₹${(val / 1000).toFixed(0)}K/year — Eligible for maximum schemes ✓`;
            incomeHint.style.color = 'var(--accent-secondary)';
        } else if (val < 300000) {
            incomeHint.textContent = `₹${(val / 100000).toFixed(1)}L/year — Eligible for many welfare schemes`;
            incomeHint.style.color = 'var(--accent-secondary)';
        } else if (val < 600000) {
            incomeHint.textContent = `₹${(val / 100000).toFixed(1)}L/year — Eligible for several schemes`;
            incomeHint.style.color = 'var(--accent-saffron)';
        } else if (val < 800000) {
            incomeHint.textContent = `₹${(val / 100000).toFixed(1)}L/year — Limited schemes available`;
            incomeHint.style.color = 'var(--accent-saffron)';
        } else {
            incomeHint.textContent = `₹${(val / 100000).toFixed(1)}L/year — Few income-based schemes`;
            incomeHint.style.color = 'var(--accent-rose)';
        }
    });
}


// ─────────── FORM SUBMISSION ───────────
async function submitForm() {
    const findBtn = document.getElementById('find-btn');
    const btnText = findBtn.querySelector('.btn-text');
    const btnLoading = findBtn.querySelector('.btn-loading');

    // Show loading state
    btnText.style.display = 'none';
    btnLoading.style.display = 'inline-flex';
    findBtn.disabled = true;

    // Collect form data
    const formData = {
        name: document.getElementById('name').value.trim(),
        age: parseInt(document.getElementById('age').value),
        gender: document.querySelector('input[name="gender"]:checked')?.value || 'other',
        state: document.getElementById('state').value,
        category: document.querySelector('input[name="category"]:checked')?.value || 'general',
        occupation: document.getElementById('occupation').value,
        annual_income: parseInt(document.getElementById('income').value) || 0,
        education: document.getElementById('education').value,
        marital_status: document.getElementById('marital_status').value,
        has_land: document.querySelector('input[name="has_land"]:checked')?.value === 'true',
        has_bank_account: document.querySelector('input[name="has_bank_account"]:checked')?.value === 'true',
        disability: document.querySelector('input[name="disability"]:checked')?.value === 'true',
    };

    try {
        const res = await fetch('/api/find-schemes', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData),
        });

        const data = await res.json();
        matchedSchemes = data.schemes;
        renderResults(data);
    } catch (e) {
        console.error('Error:', e);
        alert('Failed to connect to the server. Make sure the backend is running on port 8000.');
    }

    // Reset button state
    btnText.style.display = 'inline-flex';
    btnLoading.style.display = 'none';
    findBtn.disabled = false;
}


// ─────────── RENDER RESULTS ───────────
function renderResults(data) {
    const resultsSection = document.getElementById('results-section');
    const resultsGrid = document.getElementById('results-grid');
    const noResults = document.getElementById('no-results');
    const resultsBadge = document.getElementById('results-badge');
    const resultsTitle = document.getElementById('results-title');
    const aiSummaryText = document.getElementById('ai-summary-text');
    const resultsActions = document.getElementById('results-actions');
    const aiSummaryCard = document.getElementById('ai-summary-card');

    // Show results section
    resultsSection.style.display = 'block';

    // Update AI summary
    aiSummaryText.textContent = data.ai_summary;

    if (data.total_found === 0) {
        resultsGrid.innerHTML = '';
        noResults.style.display = 'block';
        resultsBadge.textContent = '0 Found';
        resultsTitle.textContent = 'No Matching Schemes';
        resultsActions.style.display = 'none';
        aiSummaryCard.style.display = 'block';
    } else {
        noResults.style.display = 'none';
        resultsActions.style.display = 'flex';
        aiSummaryCard.style.display = 'block';
        resultsBadge.textContent = `${data.total_found} Found`;
        resultsTitle.textContent = `${data.profile_name}, You're Eligible For ${data.total_found} Scheme${data.total_found > 1 ? 's' : ''}!`;

        // Render scheme cards
        resultsGrid.innerHTML = data.schemes.map((scheme, index) => createSchemeCard(scheme, index)).join('');
    }

    // Scroll to results
    setTimeout(() => {
        scrollToSection('results-section');
    }, 300);
}

function createSchemeCard(scheme, index) {
    const matchReasonsHTML = scheme.match_reasons.map(r => 
        `<div class="match-reason">${r}</div>`
    ).join('');

    const documentsHTML = scheme.documents.map(d => 
        `<li>${d}</li>`
    ).join('');

    return `
        <div class="scheme-card" style="animation-delay: ${index * 0.1}s" onclick="toggleSchemeDetails('${scheme.id}')">
            <div class="scheme-card-header">
                <div class="scheme-icon">${scheme.icon}</div>
                <div class="scheme-info">
                    <div class="scheme-name">${scheme.name}</div>
                    <div class="scheme-category">${scheme.category}</div>
                </div>
            </div>
            <p class="scheme-description">${scheme.description}</p>
            <div class="scheme-benefit">
                <div class="scheme-benefit-label">Potential Benefit</div>
                <div class="scheme-benefit-amount">${scheme.potential_benefit_amount}</div>
            </div>
            <div class="match-reasons">${matchReasonsHTML}</div>
            <button class="card-toggle" id="toggle-${scheme.id}" onclick="event.stopPropagation(); toggleSchemeDetails('${scheme.id}')">
                View Details
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
            </button>
            <div class="scheme-details" id="details-${scheme.id}">
                <div class="details-section">
                    <div class="details-label">💰 Full Benefits</div>
                    <div class="details-content">${scheme.benefits}</div>
                </div>
                <div class="details-section">
                    <div class="details-label">📄 Documents Required</div>
                    <ul class="document-list">${documentsHTML}</ul>
                </div>
                <div class="details-section">
                    <div class="details-label">📝 How to Apply</div>
                    <div class="details-content">${scheme.how_to_apply}</div>
                </div>
                <a href="${scheme.official_link}" target="_blank" rel="noopener noreferrer" class="scheme-link" onclick="event.stopPropagation()">
                    Visit Official Website →
                </a>
            </div>
        </div>
    `;
}

function toggleSchemeDetails(schemeId) {
    const details = document.getElementById(`details-${schemeId}`);
    const toggle = document.getElementById(`toggle-${schemeId}`);

    if (details.classList.contains('open')) {
        details.classList.remove('open');
        toggle.classList.remove('expanded');
        toggle.innerHTML = `View Details <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>`;
    } else {
        details.classList.add('open');
        toggle.classList.add('expanded');
        toggle.innerHTML = `Hide Details <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>`;
    }
}


// ─────────── AI CHAT ───────────
function toggleChat() {
    const widget = document.getElementById('chat-widget');
    const fab = document.getElementById('chat-fab');
    chatOpen = !chatOpen;

    if (chatOpen) {
        widget.classList.add('open');
        fab.style.display = 'none';
        document.getElementById('chat-input').focus();
    } else {
        widget.classList.remove('open');
        fab.style.display = 'flex';
    }
}

function initChatInput() {
    const input = document.getElementById('chat-input');
    input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') sendChatMessage();
    });
}

async function sendChatMessage() {
    const input = document.getElementById('chat-input');
    const message = input.value.trim();
    if (!message) return;

    // Clear input
    input.value = '';

    // Add user message
    appendChatMessage('user', message);

    // Show typing indicator
    const typing = document.getElementById('chat-typing');
    typing.classList.add('visible');

    // Build context from matched schemes
    let context = '';
    if (matchedSchemes.length > 0) {
        const schemeNames = matchedSchemes.map(s => s.name).join(', ');
        context = `User was matched with these schemes: ${schemeNames}`;
    }

    try {
        const res = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message, context }),
        });

        const data = await res.json();
        typing.classList.remove('visible');

        // Handle both success and error responses
        const botReply = data.response || data.detail || 'Sorry, I could not generate a response. Please try again in a few seconds.';
        appendChatMessage('bot', botReply);
    } catch (e) {
        typing.classList.remove('visible');
        appendChatMessage('bot', 'Sorry, I couldn\'t connect to the AI service. Please make sure the server is running.');
    }
}

function appendChatMessage(sender, text) {
    const messagesBox = document.getElementById('chat-messages');
    const avatar = sender === 'bot' ? '🤖' : '👤';

    const msgDiv = document.createElement('div');
    msgDiv.className = `chat-msg ${sender}`;
    msgDiv.innerHTML = `
        <div class="msg-avatar">${avatar}</div>
        <div class="msg-bubble">${escapeHTML(text)}</div>
    `;
    messagesBox.appendChild(msgDiv);
    messagesBox.scrollTop = messagesBox.scrollHeight;
}

function escapeHTML(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}


// ─────────── PDF DOWNLOAD ───────────
function downloadResultsPDF() {
    if (matchedSchemes.length === 0) return;
    
    let content = "SchemeConnect AI - Your Eligible Government Schemes\n";
    content += "=" .repeat(55) + "\n";
    content += `Generated on: ${new Date().toLocaleDateString('en-IN', { dateStyle: 'full' })}\n`;
    content += `Total Schemes Found: ${matchedSchemes.length}\n\n`;
    
    matchedSchemes.forEach((scheme, i) => {
        content += `${i + 1}. ${scheme.icon} ${scheme.name} (${scheme.short_name})\n`;
        content += `-`.repeat(50) + "\n";
        content += `   Category: ${scheme.category}\n`;
        content += `   Benefits: ${scheme.benefits}\n`;
        content += `   Potential Value: ${scheme.potential_benefit_amount}\n`;
        content += `   Documents: ${scheme.documents.join(', ')}\n`;
        content += `   How to Apply: ${scheme.how_to_apply}\n`;
        content += `   Official Website: ${scheme.official_link}\n`;
        if (scheme.match_reasons && scheme.match_reasons.length > 0) {
            content += `   Why You Qualify: ${scheme.match_reasons.join('; ')}\n`;
        }
        content += "\n";
    });
    
    content += "=" .repeat(55) + "\n";
    content += "Generated by SchemeConnect AI (schemeconnect-ai.onrender.com)\n";
    content += "Powered by Google Gemini AI | Google Solution Challenge 2026\n";
    content += "\nDisclaimer: Verify eligibility on official government websites before applying.\n";
    
    // Create and download file
    const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `SchemeConnect_Results_${new Date().toISOString().split('T')[0]}.txt`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    
    // Show feedback
    const btn = document.getElementById('download-pdf-btn');
    const original = btn.innerHTML;
    btn.innerHTML = '✅ Downloaded!';
    btn.style.background = 'linear-gradient(135deg, #10b981, #059669)';
    setTimeout(() => {
        btn.innerHTML = original;
        btn.style.background = '';
    }, 2000);
}


// ─────────── LANGUAGE TOGGLE (Hindi/English) ───────────
let currentLang = 'en';

const translations = {
    en: {
        heroTitle: 'Discover Government Schemes',
        heroGradient: 'You Deserve',
        heroSubtitle: 'India has <strong>700+ welfare schemes</strong> worth lakhs of rupees — but most citizens don\'t know which ones they qualify for. Let AI find your eligible schemes in <strong>30 seconds</strong>.',
        getStarted: 'Get Started →',
        findMySchemes: 'Find My Schemes',
        learnMore: 'Learn More',
        howItWorks: 'How It Works',
        findSchemes: 'Find Schemes',
        sectionHow: 'How It Works',
        sectionHowSub: 'Three simple steps to discover schemes worth lakhs of rupees',
        step1Title: 'Fill Your Profile',
        step1Desc: 'Answer a few simple questions about your age, occupation, income, and state. Takes under 60 seconds.',
        step2Title: 'AI Matches Schemes',
        step2Desc: 'Our Gemini AI engine analyzes your profile against 50+ government schemes to find your perfect matches.',
        step3Title: 'Get Personalized Results',
        step3Desc: 'See matching schemes with benefits, eligibility reasons, documents needed, and how to apply — all in one place.',
        formTitle: 'Find Your Schemes',
        formSubtitle: 'Fill in your details below — we\'ll match you with eligible government schemes',
        personalInfo: '👤 Personal Information',
        socialInfo: '🏷️ Social & Economic Details',
        additionalInfo: '📋 Additional Details',
        nameLabel: 'Your Name',
        ageLabel: 'Age',
        genderLabel: 'Gender',
        stateLabel: 'State / UT',
        categoryLabel: 'Category',
        occupationLabel: 'Occupation',
        incomeLabel: 'Annual Family Income (₹)',
        nextStep: 'Next Step',
        back: 'Back',
        findBtn: '🔍 Find My Schemes',
        modifyProfile: 'Modify Profile',
        downloadPdf: '📄 Download as PDF',
        askAi: '💬 Ask AI About Schemes',
        chatTitle: 'SchemeConnect AI',
    },
    hi: {
        heroTitle: 'सरकारी योजनाएं खोजें',
        heroGradient: 'जो आपका हक है',
        heroSubtitle: 'भारत में <strong>700+ कल्याणकारी योजनाएं</strong> लाखों रुपये की हैं — लेकिन अधिकांश नागरिक नहीं जानते कि वे किसके लिए पात्र हैं। AI को <strong>30 सेकंड</strong> में आपकी योजनाएं खोजने दें।',
        getStarted: 'शुरू करें →',
        findMySchemes: 'मेरी योजनाएं खोजें',
        learnMore: 'और जानें',
        howItWorks: 'कैसे काम करता है',
        findSchemes: 'योजनाएं खोजें',
        sectionHow: 'कैसे काम करता है',
        sectionHowSub: 'लाखों रुपये की योजनाएं खोजने के तीन आसान कदम',
        step1Title: 'प्रोफ़ाइल भरें',
        step1Desc: 'अपनी उम्र, व्यवसाय, आय और राज्य के बारे में कुछ सरल सवालों के जवाब दें। 60 सेकंड से कम समय लगेगा।',
        step2Title: 'AI योजनाएं मैच करता है',
        step2Desc: 'हमारा Gemini AI इंजन 50+ सरकारी योजनाओं के खिलाफ आपकी प्रोफ़ाइल का विश्लेषण करता है।',
        step3Title: 'व्यक्तिगत परिणाम पाएं',
        step3Desc: 'मिलान योजनाओं को लाभ, पात्रता कारण, आवश्यक दस्तावेज़ और आवेदन कैसे करें — सब एक जगह देखें।',
        formTitle: 'अपनी योजनाएं खोजें',
        formSubtitle: 'नीचे अपनी जानकारी भरें — हम आपको पात्र सरकारी योजनाओं से मिलाएंगे',
        personalInfo: '👤 व्यक्तिगत जानकारी',
        socialInfo: '🏷️ सामाजिक और आर्थिक विवरण',
        additionalInfo: '📋 अतिरिक्त विवरण',
        nameLabel: 'आपका नाम',
        ageLabel: 'उम्र',
        genderLabel: 'लिंग',
        stateLabel: 'राज्य / केंद्र शासित प्रदेश',
        categoryLabel: 'श्रेणी',
        occupationLabel: 'व्यवसाय',
        incomeLabel: 'वार्षिक पारिवारिक आय (₹)',
        nextStep: 'अगला कदम',
        back: 'वापस',
        findBtn: '🔍 मेरी योजनाएं खोजें',
        modifyProfile: 'प्रोफ़ाइल बदलें',
        downloadPdf: '📄 PDF डाउनलोड करें',
        askAi: '💬 AI से पूछें',
        chatTitle: 'SchemeConnect AI',
    }
};

function setLanguage(lang) {
    currentLang = lang;
    const t = translations[lang];
    
    // Update toggle buttons
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.lang === lang);
    });
    
    // Update hero
    const heroTitle = document.querySelector('.hero-title');
    if (heroTitle) {
        heroTitle.innerHTML = `${t.heroTitle}\n<span class="hero-gradient-text">${t.heroGradient}</span>`;
    }
    const heroSub = document.querySelector('.hero-subtitle');
    if (heroSub) heroSub.innerHTML = t.heroSubtitle;
    
    // Update nav links
    const navLinks = document.querySelectorAll('.nav-link');
    if (navLinks[0]) navLinks[0].textContent = t.howItWorks;
    if (navLinks[1]) navLinks[1].textContent = t.findSchemes;
    
    // Update nav CTA
    const navCta = document.querySelector('.nav-cta');
    if (navCta) navCta.textContent = t.getStarted;
    
    // Update hero buttons
    const heroActions = document.querySelectorAll('.hero-actions button');
    if (heroActions[0]) heroActions[0].innerHTML = `${t.findMySchemes} <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>`;
    if (heroActions[1]) heroActions[1].textContent = t.learnMore;
    
    // Update "How It Works" section
    const sectionTitles = document.querySelectorAll('.section-title');
    if (sectionTitles[0]) sectionTitles[0].textContent = t.sectionHow;
    const sectionSubs = document.querySelectorAll('.section-subtitle');
    if (sectionSubs[0]) sectionSubs[0].textContent = t.sectionHowSub;
    
    // Update step cards
    const stepCards = document.querySelectorAll('.step-card');
    if (stepCards[0]) { stepCards[0].querySelector('h3').textContent = t.step1Title; stepCards[0].querySelector('p').textContent = t.step1Desc; }
    if (stepCards[1]) { stepCards[1].querySelector('h3').textContent = t.step2Title; stepCards[1].querySelector('p').textContent = t.step2Desc; }
    if (stepCards[2]) { stepCards[2].querySelector('h3').textContent = t.step3Title; stepCards[2].querySelector('p').textContent = t.step3Desc; }
    
    // Update form section
    if (sectionTitles[1]) sectionTitles[1].textContent = t.formTitle;
    if (sectionSubs[1]) sectionSubs[1].textContent = t.formSubtitle;
    
    // Update step titles
    const stepTitles = document.querySelectorAll('.step-title');
    if (stepTitles[0]) stepTitles[0].textContent = t.personalInfo;
    if (stepTitles[1]) stepTitles[1].textContent = t.socialInfo;
    if (stepTitles[2]) stepTitles[2].textContent = t.additionalInfo;
    
    // Update form labels
    const nameInput = document.getElementById('name');
    if (nameInput) nameInput.placeholder = lang === 'hi' ? 'अपना नाम दर्ज करें' : 'Enter your name';
    
    // Update results actions
    const downloadBtn = document.getElementById('download-pdf-btn');
    if (downloadBtn) downloadBtn.innerHTML = t.downloadPdf;
    
    // Update chat title
    const chatTitle = document.querySelector('.chat-title');
    if (chatTitle) chatTitle.textContent = t.chatTitle;
}
