// ==================== LUNGCARE AI — MAIN APP ====================

let currentStep = 1;
const totalSteps = 5;
let isLoggedIn = false;

// ==================== INITIALIZATION ====================
document.addEventListener('DOMContentLoaded', () => {
    setupNavigation();
    setupTheme();
    setupDetailTabs();
    checkAuthState();
    setupAdminDashboard();
});

// ==================== AUTH ====================

let currentUser = null;

function checkAuthState() {
    const user = localStorage.getItem('lungcare_user');
    if (user) {
        isLoggedIn = true;
        try {
            currentUser = JSON.parse(user);
        } catch { currentUser = null; }
        showApp();
        if (currentUser && currentUser.role === 'admin') {
            document.getElementById('adminNavLink').style.display = 'inline-block';
        } else {
            document.getElementById('adminNavLink').style.display = 'none';
        }
    } else {
        showLoginPrompt();
    }
}

function showApp() {
    // Remove login overlay if present
    const loginPage = document.getElementById('loginPage');
    if (loginPage) loginPage.remove();
    document.getElementById('navbar').style.display = 'block';
    document.querySelector('.container').style.display = 'block';
    document.querySelector('.footer').style.display = 'block';
}

function showLoginPrompt() {
    document.getElementById('navbar').style.display = 'none';
    document.querySelector('.footer').style.display = 'none';
    document.querySelector('.container').style.display = 'none';

    // Remove any existing login page
    const old = document.getElementById('loginPage');
    if (old) old.remove();

    // Build particles HTML
    let particles = '';
    for (let i = 0; i < 30; i++) {
        const x = Math.random() * 100;
        const delay = Math.random() * 8;
        const dur = 6 + Math.random() * 8;
        const size = 2 + Math.random() * 3;
        particles += `<div class="login-particle" style="left:${x}%;width:${size}px;height:${size}px;animation-delay:${delay}s;animation-duration:${dur}s"></div>`;
    }

    const loginPage = document.createElement('div');
    loginPage.id = 'loginPage';
    loginPage.className = 'login-page';
    loginPage.innerHTML = `
        <div class="login-particles">${particles}</div>
        <div class="login-container">
            <div class="login-card">
                <div class="login-logo">
                    <span class="login-logo-icon">🫁</span>
                    <h2>LungCare <span>AI</span></h2>
                    <p>Lung Cancer Detection & Risk Assessment</p>
                </div>
                <div id="authForm">
                    <div id="loginForm">
                        <div class="form-group"><label>Username</label><input type="text" id="loginUser" placeholder="Enter your username"></div>
                        <div class="form-group"><label>Password</label><input type="password" id="loginPass" placeholder="Enter your password" onkeydown="if(event.key==='Enter')handleLogin()"></div>
                        <button class="btn btn-primary" onclick="handleLogin()">🔐 Sign In</button>
                        <div class="login-switch">Don't have an account? <a onclick="showRegForm()">Create one</a></div>
                    </div>
                    <div id="regForm" style="display:none">
                        <div class="form-group"><label>Username</label><input type="text" id="regUser" placeholder="Choose a username"></div>
                        <div class="form-group"><label>Email</label><input type="email" id="regEmail" placeholder="your@email.com"></div>
                        <div class="form-group"><label>Password</label><input type="password" id="regPass" placeholder="Min 6 characters" onkeydown="if(event.key==='Enter')handleRegister()"></div>
                        <button class="btn btn-primary" onclick="handleRegister()">🚀 Create Account</button>
                        <div class="login-switch">Already have an account? <a onclick="showLoginForm()">Sign in</a></div>
                    </div>
                </div>
                <div class="login-features">
                    <div class="login-feature"><span>🔬</span>Risk Analysis</div>
                    <div class="login-feature"><span>💊</span>Treatments</div>
                    <div class="login-feature"><span>🛡️</span>Precautions</div>
                    <div class="login-feature"><span>📊</span>Reports</div>
                </div>
            </div>
        </div>`;
    document.body.appendChild(loginPage);
}

function showRegForm() {
    document.getElementById('loginForm').style.display = 'none';
    document.getElementById('regForm').style.display = 'block';
}

function showLoginForm() {
    document.getElementById('regForm').style.display = 'none';
    document.getElementById('loginForm').style.display = 'block';
}

async function handleLogin() {
    const username = document.getElementById('loginUser').value.trim();
    const password = document.getElementById('loginPass').value;
    if (!username || !password) return showAlert('Please fill all fields', 'error');
    try {
        const res = await fetch('/api/auth/login', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ username, password }), credentials: 'include' });
        const data = await res.json();
        if (res.ok) {
            localStorage.setItem('lungcare_user', JSON.stringify(data));
            isLoggedIn = true;
            location.reload();
        } else { showAlert(data.error || 'Login failed', 'error'); }
    } catch (e) { showAlert('Connection error', 'error'); }
}

async function handleRegister() {
    const username = document.getElementById('regUser').value.trim();
    const email = document.getElementById('regEmail').value.trim();
    const password = document.getElementById('regPass').value;
    if (!username || !email || !password) return showAlert('Please fill all fields', 'error');
    if (password.length < 6) return showAlert('Password must be 6+ characters', 'error');
    try {
        const res = await fetch('/api/auth/register', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ username, email, password }) });
        const data = await res.json();
        if (res.ok) {
            showAlert('Registration successful! Please login.', 'success');
            showLoginForm();
        } else { showAlert(data.error || 'Registration failed', 'error'); }
    } catch (e) { showAlert('Connection error', 'error'); }
}

async function handleLogout() {
    try { await fetch('/api/auth/logout', { method: 'POST', credentials: 'include' }); } catch (e) {}
    localStorage.removeItem('lungcare_user');
    location.reload();
}

// ==================== NAVIGATION ====================
function setupNavigation() {
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const section = this.dataset.section;
            navigateTo(section);
        });
    });
    document.getElementById('logoutBtn').addEventListener('click', handleLogout);
}


function navigateTo(sectionId) {
    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
    const el = document.getElementById(sectionId);
    if (el) el.classList.add('active');
    document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
    const activeLink = document.querySelector(`.nav-link[data-section="${sectionId}"]`);
    if (activeLink) activeLink.classList.add('active');
    if (sectionId === 'history') loadHistory();
    if (sectionId === 'admin') loadAdminDashboard();
    window.scrollTo({ top: 0, behavior: 'smooth' });
}
// ==================== ADMIN DASHBOARD ====================
function setupAdminDashboard() {
    // Hide admin nav by default
    const adminNav = document.getElementById('adminNavLink');
    if (adminNav) adminNav.style.display = 'none';
}

function switchAdminTab(btn) {
    document.querySelectorAll('.admin-tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.admin-tab-content').forEach(c => c.classList.remove('active'));
    btn.classList.add('active');
    const tab = document.getElementById(btn.dataset.tab);
    if (tab) tab.classList.add('active');
}

async function loadAdminDashboard() {
    // Welcome message
    if (currentUser && currentUser.username) {
        document.getElementById('adminWelcome').textContent = `Logged in as: ${currentUser.username} (admin)`;
    }

    // Load stats
    try {
        const res = await fetch('/api/admin/stats', { credentials: 'include' });
        const stats = await res.json();
        if (res.ok) {
            let statsHtml = `
                <div class="stat-card glass-card">
                    <div class="stat-label">Total Users</div>
                    <div class="stat-value">${stats.total_users}</div>
                </div>
                <div class="stat-card glass-card">
                    <div class="stat-label">Total Assessments</div>
                    <div class="stat-value">${stats.total_assessments}</div>
                </div>
                <div class="stat-card glass-card">
                    <div class="stat-label">High Risk</div>
                    <div class="stat-value" style="color:#ef4444">${stats.high_risk_count}</div>
                </div>
                <div class="stat-card glass-card">
                    <div class="stat-label">Moderate Risk</div>
                    <div class="stat-value" style="color:#f59e0b">${stats.moderate_risk_count}</div>
                </div>
            `;
            document.getElementById('adminStatsRow').innerHTML = statsHtml;
        }
    } catch (e) {}

    // Load users
    const usersCont = document.getElementById('adminUsersContainer');
    usersCont.innerHTML = '<p class="loading-text">Loading users...</p>';
    try {
        const res = await fetch('/api/admin/users', { credentials: 'include' });
        const data = await res.json();
        if (res.ok) {
            usersCont.innerHTML = renderAdminUsers(data.users);
        } else {
            usersCont.innerHTML = `<p class="error-text">${data.error||'Failed to load users.'}</p>`;
        }
    } catch (e) {
        usersCont.innerHTML = `<p class="error-text">Error loading users.</p>`;
    }

    // Load assessments
    const assessCont = document.getElementById('adminAssessmentsContainer');
    assessCont.innerHTML = '<p class="loading-text">Loading assessments...</p>';
    try {
        const res = await fetch('/api/admin/assessments', { credentials: 'include' });
        const data = await res.json();
        if (res.ok) {
            assessCont.innerHTML = renderAdminAssessments(data.assessments);
        } else {
            assessCont.innerHTML = `<p class="error-text">${data.error||'Failed to load assessments.'}</p>`;
        }
    } catch (e) {
        assessCont.innerHTML = `<p class="error-text">Error loading assessments.</p>`;
    }

    // Load audit logs
    const logsCont = document.getElementById('adminLogsContainer');
    try {
        const res = await fetch('/api/admin/audit-logs', { credentials: 'include' });
        const data = await res.json();
        if (res.ok) {
            logsCont.innerHTML = renderAuditLogs(data.logs);
        } else {
            logsCont.innerHTML = `<p class="error-text">${data.error||'Failed to load logs.'}</p>`;
        }
    } catch (e) {
        logsCont.innerHTML = `<p class="error-text">Error loading logs.</p>`;
    }

    // Setup search
    document.getElementById('userSearchBox').addEventListener('input', debounce(adminSearchUsers, 300));
    document.getElementById('assessSearchBox').addEventListener('input', debounce(adminSearchAssessments, 300));
}

function renderAdminUsers(users) {
    if (!users || users.length === 0) return '<p>No users found.</p>';
    let html = `<table class="admin-table"><thead><tr><th>ID</th><th>Username</th><th>Email</th><th>Role</th><th>Created</th><th>Assessments</th><th>Actions</th></tr></thead><tbody>`;
    for (const u of users) {
        html += `<tr>
            <td>${u.id}</td>
            <td>${u.username}</td>
            <td>${u.email}</td>
            <td>${u.role}</td>
            <td>${u.created_at.split('T')[0]}</td>
            <td>${u.assessment_count}</td>
            <td>
                <button class="admin-btn" onclick="adminChangeRole(${u.id}, '${u.role === 'admin' ? 'user' : 'admin'}')">${u.role === 'admin' ? 'Demote' : 'Promote'}</button>
                <button class="admin-btn" onclick="adminResetPassword(${u.id})">Reset Password</button>
                <button class="admin-btn admin-danger" onclick="adminDeleteUser(${u.id})">Delete</button>
            </td>
        </tr>`;
    }
    html += '</tbody></table>';
    return html;
}

function renderAdminAssessments(assessments) {
    if (!assessments || assessments.length === 0) return '<p>No assessments found.</p>';
    let html = `<table class="admin-table"><thead><tr><th>ID</th><th>User</th><th>Prediction</th><th>Risk Level</th><th>Risk %</th><th>Date</th><th>Actions</th></tr></thead><tbody>`;
    for (const a of assessments) {
        html += `<tr>
            <td>${a.id}</td>
            <td>${a.username||a.user_id}</td>
            <td>${a.prediction}</td>
            <td>${a.risk_level}</td>
            <td>${a.cancer_risk}</td>
            <td>${a.timestamp.split('T')[0]}</td>
            <td><button class="admin-btn admin-danger" onclick="adminDeleteAssessment('${a.id}')">Delete</button></td>
        </tr>`;
    }
    html += '</tbody></table>';
    return html;
}
// Admin action handlers
async function adminChangeRole(userId, newRole) {
    if (!confirm(`Are you sure you want to change this user's role to ${newRole}?`)) return;
    try {
        const res = await fetch(`/api/admin/user/${userId}/role`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ role: newRole }),
            credentials: 'include'
        });
        const data = await res.json();
        if (res.ok) {
            showAlert('Role updated', 'success');
            loadAdminDashboard();
        } else {
            showAlert(data.error || 'Failed to update role', 'error');
        }
    } catch (e) { showAlert('Error updating role', 'error'); }
}

async function adminDeleteUser(userId) {
    if (!confirm('Are you sure you want to delete this user? This cannot be undone.')) return;
    try {
        const res = await fetch(`/api/admin/user/${userId}`, {
            method: 'DELETE',
            credentials: 'include'
        });
        const data = await res.json();
        if (res.ok) {
            showAlert('User deleted', 'success');
            loadAdminDashboard();
        } else {
            showAlert(data.error || 'Failed to delete user', 'error');
        }
    } catch (e) { showAlert('Error deleting user', 'error'); }
}

async function adminDeleteAssessment(assessmentId) {
    if (!confirm('Delete this assessment?')) return;
    try {
        const res = await fetch(`/api/admin/assessment/${assessmentId}`, {
            method: 'DELETE',
            credentials: 'include'
        });
        const data = await res.json();
        if (res.ok) {
            showAlert('Assessment deleted', 'success');
            loadAdminDashboard();
        } else {
            showAlert(data.error || 'Failed to delete assessment', 'error');
        }
    } catch (e) { showAlert('Error deleting assessment', 'error'); }
}

async function adminResetPassword(userId) {
    const newPass = prompt('Enter new password (min 6 chars):');
    if (!newPass || newPass.length < 6) return showAlert('Password must be at least 6 characters', 'error');
    try {
        const res = await fetch(`/api/admin/user/${userId}/reset-password`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ password: newPass }),
            credentials: 'include'
        });
        const data = await res.json();
        if (res.ok) {
            showAlert('Password reset', 'success');
        } else {
            showAlert(data.error || 'Failed to reset password', 'error');
        }
    } catch (e) { showAlert('Error resetting password', 'error'); }
}

// Debounce utility
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Search functions
async function adminSearchUsers() {
    const query = document.getElementById('userSearchBox').value;
    if (!query) { loadAdminDashboard(); return; }
    try {
        const res = await fetch(`/api/admin/users/search?q=${encodeURIComponent(query)}`, { credentials: 'include' });
        const data = await res.json();
        if (res.ok) {
            document.getElementById('adminUsersContainer').innerHTML = renderAdminUsers(data.users);
        }
    } catch (e) {}
}

async function adminSearchAssessments() {
    const query = document.getElementById('assessSearchBox').value;
    if (!query) { loadAdminDashboard(); return; }
    try {
        const res = await fetch(`/api/admin/assessments/search?q=${encodeURIComponent(query)}`, { credentials: 'include' });
        const data = await res.json();
        if (res.ok) {
            document.getElementById('adminAssessmentsContainer').innerHTML = renderAdminAssessments(data.assessments);
        }
    } catch (e) {}
}

// Export functions
function adminExportUsers() {
    window.location.href = '/api/admin/export/csv?type=users';
}

function adminExportAssessments() {
    window.location.href = '/api/admin/export/csv?type=assessments';
}

// Render audit logs
function renderAuditLogs(logs) {
    if (!logs || logs.length === 0) return '<p>No logs found.</p>';
    let html = `<table class="admin-table"><thead><tr><th>Admin</th><th>Action</th><th>Details</th><th>Date</th></tr></thead><tbody>`;
    for (const l of logs) {
        html += `<tr><td>${l.admin}</td><td>${l.action}</td><td>${l.details||'-'}</td><td>${l.timestamp.split('T')[0]}</td></tr>`;
    }
    html += '</tbody></table>';
    return html;
}

// ==================== THEME ====================
function setupTheme() {
    const saved = localStorage.getItem('lungcare_theme');
    if (saved === 'dark') document.documentElement.setAttribute('data-theme', 'dark');
    document.getElementById('themeToggle').addEventListener('click', () => {
        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        document.documentElement.setAttribute('data-theme', isDark ? '' : 'dark');
        localStorage.setItem('lungcare_theme', isDark ? 'light' : 'dark');
        document.getElementById('themeToggle').textContent = isDark ? '🌙' : '☀️';
    });
}

// ==================== MULTI-STEP FORM ====================
function togglePackYears() {
    const status = document.getElementById('smokingStatus').value;
    document.getElementById('packYearsGroup').style.display = (status === 'never') ? 'none' : 'block';
}

function nextStep() {
    if (currentStep === 1) {
        const age = document.getElementById('age').value;
        const gender = document.getElementById('gender').value;
        if (!age || !gender) return showAlert('Please fill in age and gender', 'error');
    }
    if (currentStep < totalSteps) {
        document.getElementById(`step-${currentStep}`).classList.remove('active');
        currentStep++;
        document.getElementById(`step-${currentStep}`).classList.add('active');
        updateProgress();
    }
}

function prevStep() {
    if (currentStep > 1) {
        document.getElementById(`step-${currentStep}`).classList.remove('active');
        currentStep--;
        document.getElementById(`step-${currentStep}`).classList.add('active');
        updateProgress();
    }
}

function updateProgress() {
    const pct = (currentStep / totalSteps) * 100;
    document.getElementById('formProgress').style.width = pct + '%';
    document.querySelectorAll('.step').forEach((s, i) => {
        s.classList.remove('active', 'completed');
        if (i + 1 < currentStep) s.classList.add('completed');
        if (i + 1 === currentStep) s.classList.add('active');
    });
    document.getElementById('prevBtn').style.display = currentStep > 1 ? 'inline-flex' : 'none';
    document.getElementById('nextBtn').style.display = currentStep < totalSteps ? 'inline-flex' : 'none';
    document.getElementById('submitBtn').style.display = currentStep === totalSteps ? 'inline-flex' : 'none';
}

// ==================== SUBMIT ASSESSMENT ====================
async function submitAssessment() {
    const data = {
        age: parseInt(document.getElementById('age').value) || 0,
        gender: document.getElementById('gender').value,
        smoking_status: document.getElementById('smokingStatus').value,
        pack_years: parseInt(document.getElementById('packYears').value) || 0,
        symptoms: getCheckedValues('symptom'),
        exposures: getCheckedValues('exposure'),
        medical_history: getCheckedValues('medical')
    };

    showLoading(true);
    try {
        const res = await fetch('/api/predict/risk-assessment', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data), credentials: 'include' });
        const result = await res.json();
        showLoading(false);
        if (res.ok) { displayResults(result); } else { showAlert(result.error || 'Assessment failed', 'error'); }
    } catch (e) {
        showLoading(false);
        showAlert('Connection error: ' + e.message, 'error');
    }
}

function getCheckedValues(name) {
    return Array.from(document.querySelectorAll(`input[name="${name}"]:checked`)).map(el => el.value);
}

// ==================== DISPLAY RESULTS ====================
function displayResults(result) {
    // Hide all modes and tabs, show results
    document.querySelectorAll('.mode-content,.mode-tabs,.form-step,.progress-container,.form-nav').forEach(el => el.classList.add('hidden'));
    document.getElementById('resultsSection').classList.remove('hidden');

    // Risk badge
    const badge = document.getElementById('riskBadge');
    badge.textContent = `${result.risk_level} Risk`;
    badge.className = `risk-badge ${result.risk_level}`;

    // Summary
    const info = result.cancer_info || {};
    document.getElementById('resultSummary').innerHTML = `
        <h3>Primary Assessment: ${info.name || result.prediction}</h3>
        <p>${info.description || ''}</p>
        <div class="result-meta">
            <div class="result-meta-item">Cancer Risk: <strong>${result.cancer_risk_percentage}%</strong></div>
            <div class="result-meta-item">Location: <strong>${info.location || 'N/A'}</strong></div>
            <div class="result-meta-item">Growth Rate: <strong>${info.growth_rate || 'N/A'}</strong></div>
            <div class="result-meta-item">Commonality: <strong>${info.commonality || 'N/A'}</strong></div>
        </div>`;

    // Score bars
    const colors = { adenocarcinoma: '#3b82f6', squamous_cell_carcinoma: '#ef4444', small_cell_lung_cancer: '#f59e0b', large_cell_carcinoma: '#8b5cf6', benign: '#10b981' };
    const labels = { adenocarcinoma: 'Adenocarcinoma', squamous_cell_carcinoma: 'Squamous Cell', small_cell_lung_cancer: 'Small Cell (SCLC)', large_cell_carcinoma: 'Large Cell', benign: 'Benign' };
    let barsHTML = '';
    const sorted = Object.entries(result.scores).sort((a, b) => b[1] - a[1]);
    for (const [key, val] of sorted) {
        barsHTML += `<div class="score-row">
            <div class="score-label">${labels[key]||key}</div>
            <div class="score-bar-track"><div class="score-bar-fill" style="width:${Math.max(val,3)}%;background:${colors[key]||'#666'}">${val}%</div></div>
            <div class="score-value">${val}%</div>
        </div>`;
    }
    document.getElementById('scoreBars').innerHTML = barsHTML;

    // Precautions
    const precautions = info.precautions || [];
    document.getElementById('precautions-tab').innerHTML = precautions.map((p, i) =>
        `<div class="detail-item"><div class="detail-num">${i+1}</div><div class="detail-text">${p}</div></div>`
    ).join('') || '<p>No precautions available.</p>';

    // Treatments
    const treatments = info.treatments || [];
    document.getElementById('treatments-tab').innerHTML = treatments.map((t, i) =>
        `<div class="detail-item"><div class="detail-num">${i+1}</div><div class="detail-text"><strong>${t.name}</strong><span>${t.description}</span><div class="treatment-stage">${t.stage}</div></div></div>`
    ).join('') || '<p>No treatment info available.</p>';

    // Medicines
    const medicines = info.medicines || [];
    document.getElementById('medicines-tab').innerHTML = medicines.map((m, i) =>
        `<div class="detail-item"><div class="detail-num">${i+1}</div><div class="detail-text"><strong>${m.name}</strong><div class="medicine-class">${m.class}</div><span>${m.usage}</span></div></div>`
    ).join('') || '<p>No medicine info available.</p>';

    window.scrollTo({ top: document.getElementById('resultsSection').offsetTop - 80, behavior: 'smooth' });
}

function resetAssessment() {
    currentStep = 1;
    document.getElementById('resultsSection').classList.add('hidden');
    // Restore mode tabs and form mode
    document.querySelectorAll('.mode-tabs').forEach(el => el.classList.remove('hidden'));
    document.querySelectorAll('.mode-content').forEach(el => el.classList.remove('active', 'hidden'));
    document.getElementById('mode-form').classList.add('active');
    document.querySelectorAll('.mode-tab').forEach((t, i) => { t.classList.toggle('active', i === 0); });
    document.querySelectorAll('.form-step,.progress-container,.form-nav').forEach(el => el.classList.remove('hidden'));
    document.querySelectorAll('.form-step').forEach(s => s.classList.remove('active'));
    document.getElementById('step-1').classList.add('active');
    document.querySelectorAll('input[type="checkbox"]:checked').forEach(cb => cb.checked = false);
    document.getElementById('age').value = '';
    document.getElementById('gender').value = '';
    document.getElementById('smokingStatus').value = 'never';
    document.getElementById('packYears').value = '0';
    togglePackYears();
    updateProgress();
    // Reset uploads
    clearImage();
    selectedCsvFile = null;
    const csvInfo = document.getElementById('csvInfo');
    if (csvInfo) csvInfo.classList.add('hidden');
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// ==================== DETAIL TABS ====================
function setupDetailTabs() {
    document.querySelectorAll('.detail-tab').forEach(tab => {
        tab.addEventListener('click', function() {
            document.querySelectorAll('.detail-tab').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.detail-content').forEach(c => c.classList.add('hidden'));
            this.classList.add('active');
            document.getElementById(this.dataset.tab).classList.remove('hidden');
        });
    });
}

// ==================== HISTORY ====================
async function loadHistory() {
    const container = document.getElementById('historyContainer');
    try {
        const res = await fetch('/api/history', { credentials: 'include' });
        const data = await res.json();
        if (!res.ok) { container.innerHTML = '<div class="empty-state">Please login to view history.</div>'; return; }
        const list = data.history || [];
        if (list.length === 0) { container.innerHTML = '<div class="empty-state">🫁 No assessments yet. Start your first risk assessment!</div>'; return; }
        const riskColors = { minimal: '#059669', low: '#ca8a04', moderate: '#ea580c', high: '#dc2626' };
        container.innerHTML = list.map(a => `
            <div class="history-card">
                <div class="history-info">
                    <h4>${a.cancer_name}</h4>
                    <p>${new Date(a.timestamp).toLocaleDateString('en-US',{year:'numeric',month:'short',day:'numeric',hour:'2-digit',minute:'2-digit'})}</p>
                </div>
                <div class="history-meta">
                    <span>Risk: ${a.cancer_risk}%</span>
                    <span class="history-risk" style="background:${riskColors[a.risk_level]||'#666'}22;color:${riskColors[a.risk_level]||'#666'};border:1px solid ${riskColors[a.risk_level]||'#666'}44">${a.risk_level}</span>
                </div>
            </div>`).join('');
    } catch (e) { container.innerHTML = '<div class="empty-state">Failed to load history.</div>'; }
}

// ==================== MODE SWITCHING ====================
function switchMode(mode) {
    document.querySelectorAll('.mode-content').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.mode-tab').forEach(el => el.classList.remove('active'));
    const modeEl = document.getElementById('mode-' + mode);
    if (modeEl) modeEl.classList.add('active');
    event.target.closest('.mode-tab').classList.add('active');
    // Hide results when switching modes
    document.getElementById('resultsSection').classList.add('hidden');
}

// ==================== IMAGE UPLOAD ====================
let selectedImageFile = null;

function handleImageSelect(input) {
    const file = input.files[0];
    if (!file) return;
    if (!file.type.startsWith('image/')) return showAlert('Please select an image file', 'error');
    if (file.size > 10 * 1024 * 1024) return showAlert('File too large (max 10MB)', 'error');
    selectedImageFile = file;
    const reader = new FileReader();
    reader.onload = function(e) {
        document.getElementById('previewImg').src = e.target.result;
        document.getElementById('imagePreview').classList.remove('hidden');
        document.getElementById('imageDropZone').style.display = 'none';
    };
    reader.readAsDataURL(file);
}

function clearImage() {
    selectedImageFile = null;
    document.getElementById('imageInput').value = '';
    document.getElementById('imagePreview').classList.add('hidden');
    document.getElementById('imageDropZone').style.display = 'block';
}

async function submitImageAnalysis() {
    if (!selectedImageFile) return showAlert('Please upload an image first', 'error');
    const formData = new FormData();
    formData.append('file', selectedImageFile);
    showLoading(true);
    try {
        const res = await fetch('/api/predict/image', { method: 'POST', body: formData, credentials: 'include' });
        const result = await res.json();
        showLoading(false);
        if (res.ok) { displayResults(result); } else { showAlert(result.error || 'Image analysis failed', 'error'); }
    } catch (e) {
        showLoading(false);
        showAlert('Connection error', 'error');
    }
}

// ==================== CSV UPLOAD ====================
let selectedCsvFile = null;

function handleCsvSelect(input) {
    const file = input.files[0];
    if (!file) return;
    selectedCsvFile = file;
    const reader = new FileReader();
    reader.onload = function(e) {
        const lines = e.target.result.split('\n').filter(l => l.trim());
        const cols = lines[0] ? lines[0].split(',').length : 0;
        document.getElementById('csvInfo').innerHTML = `
            <strong>📄 ${file.name}</strong><br>
            <span>${lines.length} rows • ${cols} columns • ${(file.size/1024).toFixed(1)} KB</span>`;
        document.getElementById('csvInfo').classList.remove('hidden');
    };
    reader.readAsText(file);
}

async function submitCsvAnalysis() {
    if (!selectedCsvFile) return showAlert('Please upload a CSV file first', 'error');
    const formData = new FormData();
    formData.append('file', selectedCsvFile);
    showLoading(true);
    try {
        const res = await fetch('/api/predict/csv', { method: 'POST', body: formData, credentials: 'include' });
        const result = await res.json();
        showLoading(false);
        if (res.ok) { displayResults(result); } else { showAlert(result.error || 'CSV analysis failed', 'error'); }
    } catch (e) {
        showLoading(false);
        showAlert('Connection error', 'error');
    }
}

// ==================== AI CHATBOT ====================
function sendSuggestion(text) {
    document.getElementById('chatInput').value = text;
    sendChat();
}

async function sendChat() {
    const input = document.getElementById('chatInput');
    const msg = input.value.trim();
    if (!msg) return;
    input.value = '';

    // Hide suggestions after first message
    const suggestions = document.getElementById('chatSuggestions');
    if (suggestions) suggestions.style.display = 'none';

    // Add user message
    addChatMessage(msg, 'user');

    // Show typing indicator
    const chatBox = document.getElementById('chatMessages');
    const typing = document.createElement('div');
    typing.className = 'chat-msg bot';
    typing.id = 'typingIndicator';
    typing.innerHTML = '<div class="chat-avatar">🤖</div><div class="chat-bubble"><div class="chat-typing"><span></span><span></span><span></span></div></div>';
    chatBox.appendChild(typing);
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        const res = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: msg }),
            credentials: 'include'
        });
        const data = await res.json();

        // Remove typing indicator
        const ti = document.getElementById('typingIndicator');
        if (ti) ti.remove();

        if (res.ok) {
            addChatMessage(data.response, 'bot');
        } else {
            addChatMessage('Sorry, I encountered an error. Please try again.', 'bot');
        }
    } catch (e) {
        const ti = document.getElementById('typingIndicator');
        if (ti) ti.remove();
        addChatMessage('Connection error. Please make sure the server is running.', 'bot');
    }
}

function addChatMessage(text, sender) {
    const chatBox = document.getElementById('chatMessages');
    const msg = document.createElement('div');
    msg.className = `chat-msg ${sender}`;

    const avatar = sender === 'bot' ? '🤖' : '👤';

    // Convert markdown bold to HTML
    let html = text
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\n/g, '<br>');

    msg.innerHTML = `<div class="chat-avatar">${avatar}</div><div class="chat-bubble">${html}</div>`;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// ==================== UTILITY ====================
function showLoading(show) {
    document.getElementById('loadingOverlay').classList.toggle('hidden', !show);
}

function showAlert(msg, type = 'info') {
    const container = document.getElementById('alertContainer');
    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.textContent = msg;
    container.appendChild(alert);
    setTimeout(() => {
        alert.style.opacity = '0';
        setTimeout(() => alert.remove(), 300);
    }, 4000);
}