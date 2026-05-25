"""
Medical AI Chatbot — Lung Cancer Specialist
Rule-based NLP chatbot with comprehensive lung cancer knowledge.
"""

import re
import random

# ==================== KNOWLEDGE BASE ====================

RESPONSES = {
    # --- Greetings ---
    "greeting": [
        "Hello! I'm LungCare AI Assistant, your medical guide for lung cancer questions. How can I help you today?",
        "Hi there! I'm here to help with lung cancer related questions — symptoms, treatments, prevention, and more. What would you like to know?",
        "Welcome! I'm your AI medical assistant specializing in lung cancer. Feel free to ask me anything about lung health."
    ],
    "farewell": [
        "Take care! Remember, early detection saves lives. Don't hesitate to consult a doctor if you have concerns. 🫁",
        "Goodbye! Stay healthy and keep up with regular screenings if you're at risk. I'm always here if you need me.",
        "Wishing you good health! Remember — this is informational only, always consult your healthcare provider for medical decisions."
    ],

    # --- Lung Cancer Types ---
    "adenocarcinoma": [
        "**Adenocarcinoma** is the most common type of lung cancer, accounting for about 40% of all cases.\n\n"
        "📍 **Location:** Outer regions of the lungs\n"
        "👥 **Who it affects:** Most common in non-smokers and women\n"
        "📈 **Growth:** Tends to grow slower than other types\n\n"
        "**Key Features:**\n"
        "• Develops in mucus-producing cells lining the alveoli\n"
        "• Often found before it has spread due to peripheral location\n"
        "• Has several targetable genetic mutations (EGFR, ALK, ROS1, KRAS)\n\n"
        "**Treatment Options:** Surgery (early stage), targeted therapy (EGFR/ALK inhibitors), immunotherapy, chemotherapy\n\n"
        "Would you like to know about specific treatments or medicines for adenocarcinoma?"
    ],
    "squamous": [
        "**Squamous Cell Carcinoma** is the second most common lung cancer (~25-30%).\n\n"
        "📍 **Location:** Central airways (near the bronchi)\n"
        "🚬 **Primary cause:** Strongly linked to smoking history\n"
        "📈 **Growth:** Moderate — may cause airway obstruction\n\n"
        "**Key Features:**\n"
        "• Develops in flat cells lining the airways\n"
        "• May cause coughing blood due to central location\n"
        "• Can obstruct airways, causing recurring pneumonia\n"
        "• Often responds well to immunotherapy\n\n"
        "**Treatment:** Surgery, chemoradiation, immunotherapy (Keytruda/Opdivo), chemotherapy with carboplatin + paclitaxel"
    ],
    "small_cell": [
        "**Small Cell Lung Cancer (SCLC)** is the most aggressive type, accounting for ~10-15% of lung cancers.\n\n"
        "⚠️ **Severity:** Very high — grows and spreads rapidly\n"
        "🚬 **Cause:** Almost exclusively linked to heavy smoking\n"
        "📈 **Growth:** Fast — often metastasized before diagnosis\n\n"
        "**Key Features:**\n"
        "• Classified as Limited Stage or Extensive Stage (not I-IV)\n"
        "• Very sensitive to chemotherapy initially, but often recurs\n"
        "• High risk of brain metastases — prophylactic cranial irradiation may be recommended\n"
        "• Can cause paraneoplastic syndromes\n\n"
        "**Treatment:** Chemotherapy + immunotherapy (carboplatin/etoposide + atezolizumab), radiation therapy\n\n"
        "⚕️ If SCLC is suspected, seek urgent medical evaluation."
    ],
    "large_cell": [
        "**Large Cell Carcinoma** is a less common type (~5-10% of lung cancers).\n\n"
        "📍 **Location:** Can appear anywhere in the lungs\n"
        "📈 **Growth:** Fast — tends to grow and spread quickly\n\n"
        "**Key Features:**\n"
        "• A diagnosis of exclusion — when cells don't fit other NSCLC categories\n"
        "• May include large cell neuroendocrine carcinoma (aggressive subtype)\n"
        "• Biomarker testing is important for treatment decisions\n\n"
        "**Treatment:** Surgery (early stage), chemotherapy, immunotherapy, targeted therapy if mutations found"
    ],

    # --- Symptoms ---
    "symptoms": [
        "**Common Lung Cancer Symptoms:**\n\n"
        "🔴 **Warning Signs:**\n"
        "• Persistent cough that doesn't go away or worsens\n"
        "• Coughing up blood (hemoptysis) — even small amounts\n"
        "• Chest pain that worsens with deep breathing or coughing\n"
        "• Shortness of breath or wheezing\n"
        "• Unexplained weight loss\n"
        "• Chronic fatigue\n"
        "• Hoarseness or voice changes\n"
        "• Recurring respiratory infections\n\n"
        "🟡 **Advanced Symptoms:**\n"
        "• Bone pain (if spread to bones)\n"
        "• Headaches, dizziness (if spread to brain)\n"
        "• Jaundice (if spread to liver)\n"
        "• Finger clubbing\n"
        "• Swelling in face/neck (superior vena cava syndrome)\n\n"
        "⚕️ **Important:** Many early-stage lung cancers have NO symptoms. Regular screening is crucial if you're at risk."
    ],

    # --- Treatment ---
    "treatment": [
        "**Lung Cancer Treatment Options:**\n\n"
        "🔪 **Surgery:**\n"
        "• Lobectomy (removes a lobe) — most common\n"
        "• Wedge resection (removes small section)\n"
        "• Pneumonectomy (removes entire lung)\n"
        "• Best for Stage I-II\n\n"
        "💉 **Chemotherapy:**\n"
        "• Platinum-based (cisplatin/carboplatin) combinations\n"
        "• Usually 4-6 cycles\n"
        "• Used alone or with other treatments\n\n"
        "🎯 **Targeted Therapy:**\n"
        "• For specific mutations: EGFR, ALK, ROS1, KRAS G12C, BRAF, MET, RET\n"
        "• Oral pills with fewer side effects than chemo\n"
        "• Requires genomic/biomarker testing\n\n"
        "🛡️ **Immunotherapy:**\n"
        "• PD-1/PD-L1 inhibitors (Keytruda, Opdivo, Tecentriq)\n"
        "• Helps immune system fight cancer\n"
        "• Can produce durable responses\n\n"
        "☢️ **Radiation Therapy:**\n"
        "• SBRT/SABR for early-stage\n"
        "• Concurrent with chemo for locally advanced\n"
        "• Palliative for symptom relief"
    ],

    # --- Medicines ---
    "medicines": [
        "**Key Lung Cancer Medicines:**\n\n"
        "🎯 **Targeted Therapy Drugs:**\n"
        "• **Osimertinib (Tagrisso)** — EGFR mutations\n"
        "• **Alectinib (Alecensa)** — ALK rearrangements\n"
        "• **Sotorasib (Lumakras)** — KRAS G12C mutations\n"
        "• **Crizotinib (Xalkori)** — ALK/ROS1\n\n"
        "🛡️ **Immunotherapy Drugs:**\n"
        "• **Pembrolizumab (Keytruda)** — PD-1 inhibitor\n"
        "• **Nivolumab (Opdivo)** — PD-1 inhibitor\n"
        "• **Atezolizumab (Tecentriq)** — PD-L1 inhibitor\n"
        "• **Durvalumab (Imfinzi)** — PD-L1 inhibitor\n\n"
        "💉 **Chemotherapy Drugs:**\n"
        "• **Carboplatin + Pemetrexed** — adenocarcinoma\n"
        "• **Carboplatin + Paclitaxel** — squamous cell\n"
        "• **Cisplatin + Etoposide** — small cell\n\n"
        "⚕️ All medications should be prescribed by an oncologist after proper diagnosis and testing."
    ],

    # --- Prevention ---
    "prevention": [
        "**Lung Cancer Prevention Tips:**\n\n"
        "🚭 **#1 — Quit Smoking:**\n"
        "• Smoking causes ~80% of lung cancer deaths\n"
        "• Risk decreases significantly within 5-10 years of quitting\n"
        "• Seek help: nicotine patches, medications, counseling\n\n"
        "🏠 **Test for Radon:**\n"
        "• Second leading cause of lung cancer\n"
        "• Odorless gas that seeps into homes\n"
        "• Use home test kits — fix if levels > 4 pCi/L\n\n"
        "🏭 **Avoid Carcinogens:**\n"
        "• Wear protective equipment around asbestos, chemicals\n"
        "• Reduce air pollution exposure\n"
        "• Use air purifiers indoors\n\n"
        "🥗 **Healthy Lifestyle:**\n"
        "• Eat fruits and vegetables rich in antioxidants\n"
        "• Exercise regularly (30+ min/day)\n"
        "• Maintain healthy weight\n\n"
        "🔍 **Get Screened:**\n"
        "• Annual low-dose CT scan if age 50-80 with 20+ pack-year smoking history\n"
        "• Early detection improves survival dramatically"
    ],

    # --- Screening ---
    "screening": [
        "**Lung Cancer Screening Guidelines:**\n\n"
        "The U.S. Preventive Services Task Force (USPSTF) recommends:\n\n"
        "✅ **Who should get screened:**\n"
        "• Age 50 to 80 years\n"
        "• 20+ pack-year smoking history\n"
        "• Currently smoke or quit within past 15 years\n\n"
        "🩻 **How:** Annual low-dose CT scan (LDCT)\n"
        "• Quick, painless, ~30 seconds\n"
        "• Low radiation dose\n"
        "• Can detect tumors as small as 1-2mm\n\n"
        "📊 **Results:**\n"
        "• LDCT reduces lung cancer mortality by 20% in high-risk populations\n"
        "• Most findings are benign (>95%)\n"
        "• False positives require follow-up scans\n\n"
        "Talk to your doctor about whether screening is right for you."
    ],

    # --- Stages ---
    "stages": [
        "**Lung Cancer Stages:**\n\n"
        "**Non-Small Cell (NSCLC):**\n\n"
        "📗 **Stage I** — Tumor in lung only, <4cm, no lymph nodes\n"
        "• 5-year survival: 68-92%\n"
        "• Treatment: Surgery\n\n"
        "📘 **Stage II** — Tumor 4-7cm or nearby lymph nodes involved\n"
        "• 5-year survival: 53-60%\n"
        "• Treatment: Surgery + chemotherapy\n\n"
        "📙 **Stage III** — Spread to mediastinal lymph nodes\n"
        "• 5-year survival: 13-36%\n"
        "• Treatment: Chemoradiation ± surgery ± immunotherapy\n\n"
        "📕 **Stage IV** — Spread to other organs (metastatic)\n"
        "• 5-year survival: 1-10%\n"
        "• Treatment: Systemic therapy (chemo, targeted, immuno)\n\n"
        "**Small Cell (SCLC):**\n"
        "• **Limited Stage** — One side of chest (30% of cases)\n"
        "• **Extensive Stage** — Spread beyond one side (70% of cases)"
    ],

    # --- Survival / Prognosis ---
    "survival": [
        "**Lung Cancer Survival Rates:**\n\n"
        "Overall 5-year survival rate: ~25% (all stages combined)\n\n"
        "**By Stage at Diagnosis:**\n"
        "• Localized (Stage I-II): **61%** 5-year survival\n"
        "• Regional (Stage III): **35%** 5-year survival\n"
        "• Distant (Stage IV): **8%** 5-year survival\n\n"
        "**By Type:**\n"
        "• NSCLC overall: ~28%\n"
        "• SCLC overall: ~7%\n"
        "• Adenocarcinoma (caught early): up to 92%\n\n"
        "📈 **Good news:** Survival rates are improving!\n"
        "• New targeted therapies and immunotherapy have significantly improved outcomes\n"
        "• Earlier detection through screening programs\n"
        "• Personalized medicine based on genetic testing\n\n"
        "⚕️ Individual prognosis depends on many factors. Discuss with your oncologist."
    ],

    # --- Risk factors ---
    "risk_factors": [
        "**Lung Cancer Risk Factors:**\n\n"
        "🔴 **High Risk:**\n"
        "• **Smoking** — #1 cause (15-30x increased risk)\n"
        "• **Secondhand smoke** — ~7,000 deaths/year in non-smokers\n"
        "• **Radon exposure** — #1 cause in non-smokers\n"
        "• **Asbestos exposure** — especially combined with smoking\n"
        "• **Family history** of lung cancer\n\n"
        "🟡 **Moderate Risk:**\n"
        "• Previous radiation to chest\n"
        "• COPD or pulmonary fibrosis\n"
        "• Occupational chemicals (arsenic, diesel, silica)\n"
        "• Air pollution (PM2.5 particles)\n"
        "• Previous cancer history\n\n"
        "🟢 **Protective Factors:**\n"
        "• Never smoking\n"
        "• Regular physical activity\n"
        "• Diet rich in fruits and vegetables\n"
        "• Low radon home environment"
    ],

    # --- Diet ---
    "diet": [
        "**Diet & Nutrition for Lung Health:**\n\n"
        "🥗 **Cancer-Fighting Foods:**\n"
        "• **Cruciferous vegetables** — broccoli, cauliflower, cabbage (contain sulforaphane)\n"
        "• **Berries** — blueberries, strawberries (rich in antioxidants)\n"
        "• **Leafy greens** — spinach, kale (folate, carotenoids)\n"
        "• **Tomatoes** — lycopene (powerful antioxidant)\n"
        "• **Green tea** — EGCG (anti-cancer properties)\n"
        "• **Turmeric** — curcumin (anti-inflammatory)\n"
        "• **Garlic & onions** — allicin compounds\n\n"
        "🚫 **Foods to Limit:**\n"
        "• Processed meats (bacon, sausage, hot dogs)\n"
        "• Red meat in excess\n"
        "• Alcohol\n"
        "• Processed/fried foods\n"
        "• Sugary drinks\n\n"
        "💊 **Note:** No supplement can replace a healthy diet. Avoid high-dose beta-carotene supplements if you smoke — they may increase risk."
    ],

    # --- Fallback ---
    "unknown": [
        "I'm not sure I understand that question. I can help with:\n\n"
        "• **Lung cancer types** — adenocarcinoma, squamous cell, small cell, large cell\n"
        "• **Symptoms** — warning signs to watch for\n"
        "• **Treatments** — surgery, chemo, immunotherapy, targeted therapy\n"
        "• **Medicines** — specific drugs and their uses\n"
        "• **Prevention** — how to reduce your risk\n"
        "• **Screening** — who should get screened and how\n"
        "• **Stages** — what each stage means\n"
        "• **Survival rates** — prognosis information\n"
        "• **Risk factors** — what increases your risk\n"
        "• **Diet** — nutrition for lung health\n\n"
        "Try asking something like: *'What are the symptoms of lung cancer?'* or *'Tell me about immunotherapy'*"
    ],

    # --- Emergency ---
    "emergency": [
        "⚠️ **If you are experiencing a medical emergency, please call your local emergency number immediately (911 in the US).**\n\n"
        "**Seek immediate medical attention if you have:**\n"
        "• Severe difficulty breathing\n"
        "• Coughing up large amounts of blood\n"
        "• Sudden severe chest pain\n"
        "• Confusion or loss of consciousness\n"
        "• High fever with respiratory symptoms\n\n"
        "I am an AI assistant and cannot provide emergency medical care. Please contact a healthcare professional immediately."
    ],

    # --- Immunotherapy ---
    "immunotherapy": [
        "**Immunotherapy for Lung Cancer:**\n\n"
        "Immunotherapy helps your immune system recognize and fight cancer cells. It has revolutionized lung cancer treatment.\n\n"
        "🛡️ **How it works:**\n"
        "Cancer cells hide from the immune system using checkpoint proteins (PD-1/PD-L1). Immunotherapy drugs block these proteins, \"unmasking\" the cancer.\n\n"
        "💊 **Key Drugs:**\n"
        "• **Pembrolizumab (Keytruda)** — Most widely used; PD-1 inhibitor\n"
        "• **Nivolumab (Opdivo)** — PD-1 inhibitor; used alone or with ipilimumab\n"
        "• **Atezolizumab (Tecentriq)** — PD-L1 inhibitor; used in NSCLC and SCLC\n"
        "• **Durvalumab (Imfinzi)** — PD-L1 inhibitor; after chemoradiation\n\n"
        "✅ **Best candidates:** High PD-L1 expression (≥50%) tumors\n"
        "⏱️ **Duration:** Usually given every 3-6 weeks for up to 2 years\n"
        "📊 **Response rate:** 30-45% in selected patients\n\n"
        "**Side Effects:** Fatigue, skin rash, pneumonitis, thyroid issues, colitis"
    ],

    # --- Chemotherapy ---
    "chemotherapy": [
        "**Chemotherapy for Lung Cancer:**\n\n"
        "💉 **What it is:** Drugs that kill rapidly dividing cells throughout the body.\n\n"
        "**Common Regimens:**\n"
        "• **Adenocarcinoma:** Carboplatin + Pemetrexed (4-6 cycles)\n"
        "• **Squamous Cell:** Carboplatin + Paclitaxel or Gemcitabine\n"
        "• **Small Cell:** Cisplatin/Carboplatin + Etoposide\n\n"
        "**Side Effects:**\n"
        "• Nausea/vomiting (managed with anti-nausea meds)\n"
        "• Hair loss\n"
        "• Fatigue\n"
        "• Low blood counts (increased infection risk)\n"
        "• Neuropathy (numbness in hands/feet)\n\n"
        "**Duration:** Usually 4-6 cycles, each cycle 3-4 weeks\n"
        "**Setting:** IV infusion in hospital/clinic, some oral options\n\n"
        "⚕️ Often combined with immunotherapy for better outcomes."
    ],

    # --- Smoking ---
    "smoking": [
        "**Smoking & Lung Cancer:**\n\n"
        "🚬 **The Facts:**\n"
        "• Smoking causes 80-90% of lung cancer cases\n"
        "• Risk increases with duration and intensity (pack-years)\n"
        "• Even 1-4 cigarettes/day significantly increases risk\n"
        "• Secondhand smoke causes ~7,000 lung cancer deaths/year\n\n"
        "📉 **After Quitting:**\n"
        "• Risk begins to decrease within 5 years\n"
        "• After 10 years: risk drops to ~50% of a current smoker\n"
        "• After 15 years: risk approaches (but never equals) a never-smoker\n\n"
        "🆘 **How to Quit:**\n"
        "• Nicotine replacement (patches, gum, lozenges)\n"
        "• Medications: Varenicline (Chantix), Bupropion (Wellbutrin)\n"
        "• Behavioral counseling\n"
        "• Quit lines: 1-800-QUIT-NOW (US)\n"
        "• Apps: QuitNow!, Smoke Free\n\n"
        "💪 It's NEVER too late to quit. Your lungs start healing within hours."
    ],
}

# ==================== INTENT DETECTION ====================

INTENT_PATTERNS = {
    "greeting": r'\b(hello|hi|hey|good\s*(morning|afternoon|evening)|greetings|howdy|sup)\b',
    "farewell": r'\b(bye|goodbye|see\s*you|take\s*care|exit|quit|thanks|thank\s*you)\b',
    "emergency": r'\b(emergency|dying|can\'t\s*breathe|call\s*911|urgent|ambulance|help\s*me)\b',
    "adenocarcinoma": r'\b(adenocarcinoma|adeno\s*carcinoma)\b',
    "squamous": r'\b(squamous|squamous\s*cell)\b',
    "small_cell": r'\b(small\s*cell|sclc)\b',
    "large_cell": r'\b(large\s*cell)\b',
    "symptoms": r'\b(symptom|sign|warning\s*sign|how\s*(do\s*i|to)\s*know|feel|indicator|what\s*are\s*the\s*sign|what\s*happens)\b',
    "treatment": r'\b(treatment|treat|cure|therap|how\s*(is\s*it|to)\s*treat|option|what\s*can\s*(be\s*done|i\s*do))\b',
    "medicines": r'\b(medicine|medication|drug|pharma|prescri|pill|tablet|what\s*(drug|medicine))\b',
    "immunotherapy": r'\b(immunotherapy|immuno|keytruda|opdivo|tecentriq|pd[\-\s]*[l1]|checkpoint)\b',
    "chemotherapy": r'\b(chemotherapy|chemo)\b',
    "prevention": r'\b(prevent|avoid|reduce\s*risk|lower\s*risk|protect|how\s*to\s*(not|avoid|prevent))\b',
    "screening": r'\b(screen|scan|ct\s*scan|ldct|detect|test|diagnos|check|found|x[\-\s]*ray)\b',
    "stages": r'\b(stage|staging|stage\s*[1234iv]|tnm|how\s*far|spread)\b',
    "survival": r'\b(surviv|prognos|life\s*expectan|how\s*long|mortality|death\s*rate|chance|outlook|fatal)\b',
    "risk_factors": r'\b(risk\s*factor|cause|what\s*causes|why\s*(do|does)|who\s*gets|suscept|predispos)\b',
    "smoking": r'\b(smok|cigarette|tobacco|nicotine|vap|e[\-\s]*cig|quit\s*smok)\b',
    "diet": r'\b(diet|food|eat|nutrition|supplement|vitamin|what\s*to\s*eat|healthy\s*food)\b',
}


def get_response(message):
    """Process user message and return appropriate medical response."""
    msg = message.lower().strip()

    if not msg:
        return random.choice(RESPONSES["unknown"])

    # Check emergency first
    if re.search(INTENT_PATTERNS["emergency"], msg):
        return random.choice(RESPONSES["emergency"])

    # Check all intents
    matched_intent = None
    for intent, pattern in INTENT_PATTERNS.items():
        if re.search(pattern, msg):
            matched_intent = intent
            # Don't break on greeting/farewell if more specific intent exists
            if intent not in ("greeting", "farewell"):
                break

    if matched_intent and matched_intent in RESPONSES:
        return random.choice(RESPONSES[matched_intent])

    # Check for general lung cancer question
    if re.search(r'\b(lung\s*cancer|cancer|tumor|tumour|malignan|oncolog)\b', msg):
        # Try to determine what aspect
        if re.search(r'\b(type|kind|form|classification|categor)\b', msg):
            return ("**Types of Lung Cancer:**\n\n"
                    "There are two main categories:\n\n"
                    "**Non-Small Cell (NSCLC) — 85% of cases:**\n"
                    "1. **Adenocarcinoma** (~40%) — Most common, often in non-smokers\n"
                    "2. **Squamous Cell** (~25-30%) — Linked to smoking\n"
                    "3. **Large Cell** (~5-10%) — Can appear anywhere\n\n"
                    "**Small Cell (SCLC) — 15% of cases:**\n"
                    "• Very aggressive, almost always smoking-related\n\n"
                    "Would you like details about any specific type?")
        return random.choice(RESPONSES["symptoms"])

    # Fallback
    return random.choice(RESPONSES["unknown"])
