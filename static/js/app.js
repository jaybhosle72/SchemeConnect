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
