"""
Medical Knowledge Base for Lung Cancer Detection System
Contains cancer type information, risk factors, treatments, and risk scoring algorithm.
"""


# ==================== CANCER TYPE INFORMATION ====================

CANCER_TYPES = {
    "adenocarcinoma": {
        "name": "Adenocarcinoma",
        "description": "The most common type of lung cancer, accounting for about 40% of all lung cancers. It develops in the cells that line the alveoli (air sacs) and tends to grow slower than other types. It is the most common type found in non-smokers and women.",
        "severity": "high",
        "commonality": "Most common (~40% of lung cancers)",
        "location": "Outer regions of the lungs",
        "growth_rate": "Moderate — tends to grow slower than other types",
        "precautions": [
            "Quit smoking immediately if you currently smoke",
            "Avoid secondhand smoke exposure",
            "Test your home for radon gas levels",
            "Use protective equipment if working with chemicals or asbestos",
            "Maintain regular follow-up screenings (low-dose CT scans)",
            "Maintain a healthy diet rich in fruits, vegetables, and antioxidants",
            "Exercise regularly to maintain lung health",
            "Monitor for new or worsening symptoms and report immediately",
            "Consider genetic counseling if family history is present",
            "Avoid air pollution — use air purifiers indoors"
        ],
        "treatments": [
            {
                "name": "Surgery",
                "description": "Lobectomy (removal of a lobe), wedge resection, or pneumonectomy depending on stage. Often the first-line treatment for early-stage disease.",
                "stage": "Stage I-II (Early)"
            },
            {
                "name": "Targeted Therapy",
                "description": "Drugs that target specific genetic mutations (EGFR, ALK, ROS1, KRAS G12C). Genomic testing is essential to identify actionable mutations.",
                "stage": "Stage III-IV (Advanced)"
            },
            {
                "name": "Immunotherapy",
                "description": "Checkpoint inhibitors (PD-1/PD-L1) help the immune system recognize and attack cancer cells. Often used as first-line for advanced disease without targetable mutations.",
                "stage": "Stage III-IV (Advanced)"
            },
            {
                "name": "Chemotherapy",
                "description": "Platinum-based combination chemotherapy (cisplatin or carboplatin with pemetrexed). May be used alone or combined with immunotherapy.",
                "stage": "Stage II-IV"
            },
            {
                "name": "Radiation Therapy",
                "description": "Stereotactic body radiation therapy (SBRT) for early-stage or conventional radiation for locally advanced disease. Can be curative or palliative.",
                "stage": "All stages"
            }
        ],
        "medicines": [
            {"name": "Osimertinib (Tagrisso)", "class": "EGFR Inhibitor", "usage": "First-line for EGFR-mutated adenocarcinoma"},
            {"name": "Alectinib (Alecensa)", "class": "ALK Inhibitor", "usage": "First-line for ALK-positive adenocarcinoma"},
            {"name": "Pembrolizumab (Keytruda)", "class": "PD-1 Inhibitor", "usage": "Immunotherapy for PD-L1 positive tumors"},
            {"name": "Carboplatin + Pemetrexed", "class": "Chemotherapy", "usage": "Standard platinum doublet for adenocarcinoma"},
            {"name": "Bevacizumab (Avastin)", "class": "Anti-VEGF", "usage": "Targets blood vessel growth in tumors"},
            {"name": "Sotorasib (Lumakras)", "class": "KRAS G12C Inhibitor", "usage": "For KRAS G12C mutated tumors"}
        ]
    },

    "squamous_cell_carcinoma": {
        "name": "Squamous Cell Carcinoma",
        "description": "The second most common type of lung cancer (~25-30%). It develops in the flat cells lining the airways (bronchi) and is strongly associated with smoking history. Often found in the central part of the lungs near the main bronchi.",
        "severity": "high",
        "commonality": "Second most common (~25-30% of lung cancers)",
        "location": "Central airways of the lungs",
        "growth_rate": "Moderate — may cause airway obstruction",
        "precautions": [
            "Stop smoking immediately — this is the strongest risk factor",
            "Enroll in a smoking cessation program if needed",
            "Get regular low-dose CT screening if you have a significant smoking history",
            "Avoid occupational exposure to carcinogens",
            "Report any persistent cough, blood in sputum, or chest pain immediately",
            "Maintain adequate hydration and nutrition",
            "Avoid environments with heavy air pollution",
            "Follow up regularly with your oncology team",
            "Consider pulmonary rehabilitation for breathing difficulties",
            "Stay up to date with vaccinations (flu, pneumonia)"
        ],
        "treatments": [
            {
                "name": "Surgery",
                "description": "Lobectomy or pneumonectomy for resectable tumors. Central location may require sleeve resection. Best outcomes in early-stage disease.",
                "stage": "Stage I-II (Early)"
            },
            {
                "name": "Chemoradiation",
                "description": "Concurrent chemotherapy and radiation therapy. Standard of care for locally advanced, unresectable disease.",
                "stage": "Stage III (Locally Advanced)"
            },
            {
                "name": "Immunotherapy",
                "description": "Pembrolizumab or nivolumab as monotherapy or combined with chemotherapy. Squamous cell often responds well to immunotherapy.",
                "stage": "Stage III-IV (Advanced)"
            },
            {
                "name": "Chemotherapy",
                "description": "Platinum-based regimens with gemcitabine or paclitaxel. Note: pemetrexed is NOT recommended for squamous cell.",
                "stage": "Stage II-IV"
            },
            {
                "name": "Radiation Therapy",
                "description": "Can be used as primary treatment for patients who cannot undergo surgery, or as adjuvant therapy post-surgery.",
                "stage": "All stages"
            }
        ],
        "medicines": [
            {"name": "Pembrolizumab (Keytruda)", "class": "PD-1 Inhibitor", "usage": "First-line immunotherapy, especially high PD-L1"},
            {"name": "Nivolumab (Opdivo)", "class": "PD-1 Inhibitor", "usage": "Second-line immunotherapy"},
            {"name": "Carboplatin + Paclitaxel", "class": "Chemotherapy", "usage": "Standard first-line chemotherapy for squamous cell"},
            {"name": "Gemcitabine", "class": "Chemotherapy", "usage": "Alternative combination partner with platinum"},
            {"name": "Necitumumab (Portrazza)", "class": "EGFR Antibody", "usage": "Combined with chemotherapy for metastatic squamous cell"},
            {"name": "Docetaxel", "class": "Chemotherapy", "usage": "Second-line treatment option"}
        ]
    },

    "small_cell_lung_cancer": {
        "name": "Small Cell Lung Cancer (SCLC)",
        "description": "An aggressive, fast-growing cancer that accounts for about 10-15% of lung cancers. It is almost exclusively associated with heavy smoking. SCLC tends to spread quickly to other parts of the body, often before diagnosis.",
        "severity": "very_high",
        "commonality": "~10-15% of lung cancers",
        "location": "Central airways, spreads rapidly",
        "growth_rate": "Fast — highly aggressive with early metastasis",
        "precautions": [
            "Immediate smoking cessation is critical",
            "Urgent medical evaluation — this cancer progresses rapidly",
            "Regular brain MRI scans to monitor for brain metastases",
            "Prophylactic cranial irradiation (PCI) may be recommended",
            "Monitor for paraneoplastic syndromes (hormonal imbalances)",
            "Maintain nutrition despite appetite loss",
            "Seek palliative care early for symptom management",
            "Discuss clinical trial options with your oncologist",
            "Keep emergency contacts readily available",
            "Emotional and psychological support is important"
        ],
        "treatments": [
            {
                "name": "Chemotherapy + Immunotherapy",
                "description": "First-line treatment: platinum-etoposide combined with atezolizumab or durvalumab. This is the current standard of care.",
                "stage": "Extensive Stage"
            },
            {
                "name": "Chemotherapy Alone",
                "description": "Cisplatin or carboplatin with etoposide for 4-6 cycles. Very chemosensitive initially but often recurs.",
                "stage": "Limited & Extensive Stage"
            },
            {
                "name": "Radiation Therapy",
                "description": "Concurrent thoracic radiation with chemotherapy for limited-stage disease. Prophylactic cranial irradiation (PCI) to prevent brain metastases.",
                "stage": "Limited Stage"
            },
            {
                "name": "Surgery",
                "description": "Rarely an option. Only considered for very early-stage disease (T1-T2, N0) which is uncommon at diagnosis.",
                "stage": "Very Early Stage (Rare)"
            },
            {
                "name": "Topotecan (Second-line)",
                "description": "Used when cancer returns after initial chemotherapy. Lurbinectedin is a newer second-line option.",
                "stage": "Recurrent Disease"
            }
        ],
        "medicines": [
            {"name": "Carboplatin + Etoposide", "class": "Chemotherapy", "usage": "Standard first-line combination"},
            {"name": "Atezolizumab (Tecentriq)", "class": "PD-L1 Inhibitor", "usage": "Added to chemo for extensive-stage SCLC"},
            {"name": "Durvalumab (Imfinzi)", "class": "PD-L1 Inhibitor", "usage": "Alternative immunotherapy with chemo"},
            {"name": "Topotecan", "class": "Chemotherapy", "usage": "Second-line for relapsed SCLC"},
            {"name": "Lurbinectedin (Zepzelca)", "class": "Chemotherapy", "usage": "Newer second-line option"},
            {"name": "Cisplatin + Etoposide", "class": "Chemotherapy", "usage": "Alternative platinum doublet"}
        ]
    },

    "large_cell_carcinoma": {
        "name": "Large Cell Carcinoma",
        "description": "A less common type of non-small cell lung cancer (~5-10%). It can appear in any part of the lung and tends to grow and spread quickly. It is a diagnosis of exclusion — when cancer cells don't fit other NSCLC categories.",
        "severity": "high",
        "commonality": "Less common (~5-10% of lung cancers)",
        "location": "Can appear anywhere in the lungs",
        "growth_rate": "Fast — tends to grow and spread quickly",
        "precautions": [
            "Stop smoking and avoid all tobacco products",
            "Seek immediate comprehensive staging workup",
            "Regular follow-up imaging (CT, PET scans)",
            "Maintain good nutrition to support treatment tolerance",
            "Stay physically active as tolerated",
            "Discuss all treatment options including clinical trials",
            "Monitor for neurological symptoms (brain metastases)",
            "Genetic/biomarker testing of tumor tissue is recommended",
            "Join a support group for emotional well-being",
            "Advance care planning discussions with healthcare team"
        ],
        "treatments": [
            {
                "name": "Surgery",
                "description": "Lobectomy with lymph node dissection for early-stage disease. Best chance for cure when caught early.",
                "stage": "Stage I-II (Early)"
            },
            {
                "name": "Chemotherapy",
                "description": "Platinum-based doublet chemotherapy. Similar regimens to adenocarcinoma (carboplatin + pemetrexed or paclitaxel).",
                "stage": "Stage II-IV"
            },
            {
                "name": "Immunotherapy",
                "description": "Checkpoint inhibitors, especially for PD-L1 positive tumors. Can be combined with chemotherapy.",
                "stage": "Stage III-IV (Advanced)"
            },
            {
                "name": "Radiation Therapy",
                "description": "Adjuvant radiation after surgery or definitive radiation for inoperable cases.",
                "stage": "All stages"
            },
            {
                "name": "Targeted Therapy",
                "description": "If specific mutations are found through genomic testing. Less common in large cell but should always be tested.",
                "stage": "Stage III-IV if mutations found"
            }
        ],
        "medicines": [
            {"name": "Carboplatin + Paclitaxel", "class": "Chemotherapy", "usage": "Common first-line regimen"},
            {"name": "Pembrolizumab (Keytruda)", "class": "PD-1 Inhibitor", "usage": "For PD-L1 positive tumors"},
            {"name": "Atezolizumab (Tecentriq)", "class": "PD-L1 Inhibitor", "usage": "Alternative immunotherapy option"},
            {"name": "Carboplatin + Pemetrexed", "class": "Chemotherapy", "usage": "Alternative first-line chemotherapy"},
            {"name": "Nivolumab + Ipilimumab", "class": "Dual Immunotherapy", "usage": "Combination checkpoint inhibitor therapy"},
            {"name": "Docetaxel", "class": "Chemotherapy", "usage": "Second-line treatment"}
        ]
    },

    "benign": {
        "name": "Benign Lung Condition",
        "description": "No evidence of malignancy detected. Benign lung nodules are non-cancerous growths that can result from infections, inflammation, or other non-malignant causes. While reassuring, continued monitoring may be recommended.",
        "severity": "low",
        "commonality": "Very common — most lung nodules are benign",
        "location": "Can appear anywhere in the lungs",
        "growth_rate": "Stable or very slow growing",
        "precautions": [
            "Continue regular health checkups and screenings",
            "Follow up with your doctor for monitoring if a nodule was found",
            "Quit smoking to reduce future cancer risk",
            "Maintain a healthy, active lifestyle",
            "Eat a balanced diet rich in antioxidants",
            "Get annual flu and pneumonia vaccinations",
            "Report any new respiratory symptoms promptly",
            "Reduce exposure to environmental pollutants",
            "Manage chronic conditions (asthma, COPD) effectively",
            "Practice deep breathing exercises for lung health"
        ],
        "treatments": [
            {
                "name": "Observation / Watchful Waiting",
                "description": "For stable, small nodules — periodic CT scans to monitor for changes over 1-2 years.",
                "stage": "Standard approach"
            },
            {
                "name": "Antibiotics",
                "description": "If the nodule is related to a bacterial infection (e.g., pneumonia, tuberculosis granuloma).",
                "stage": "If infection-related"
            },
            {
                "name": "Anti-inflammatory Treatment",
                "description": "For inflammatory conditions like sarcoidosis or rheumatoid nodules.",
                "stage": "If inflammation-related"
            },
            {
                "name": "Surgical Removal",
                "description": "Rarely needed. Only if the nodule is large, growing, or causing symptoms.",
                "stage": "If symptomatic or growing"
            }
        ],
        "medicines": [
            {"name": "No cancer medications needed", "class": "N/A", "usage": "Benign conditions do not require oncology treatment"},
            {"name": "Antibiotics (if infection)", "class": "Antimicrobial", "usage": "Amoxicillin, Azithromycin for bacterial causes"},
            {"name": "Anti-inflammatory drugs", "class": "NSAID/Corticosteroid", "usage": "For inflammation-related nodules"},
            {"name": "Bronchodilators", "class": "Respiratory", "usage": "If associated with COPD or asthma symptoms"}
        ]
    }
}


# ==================== RISK FACTOR WEIGHTS ====================

# Risk scoring weights for lung cancer type prediction
# Based on epidemiological data and medical literature

RISK_WEIGHTS = {
    # Smoking-related factors
    "smoking_status": {
        "current": {"squamous_cell_carcinoma": 0.35, "small_cell_lung_cancer": 0.40, "adenocarcinoma": 0.15, "large_cell_carcinoma": 0.20},
        "former": {"squamous_cell_carcinoma": 0.20, "small_cell_lung_cancer": 0.20, "adenocarcinoma": 0.15, "large_cell_carcinoma": 0.12},
        "never": {"adenocarcinoma": 0.30, "squamous_cell_carcinoma": 0.02, "small_cell_lung_cancer": 0.01, "large_cell_carcinoma": 0.05}
    },
    "pack_years": {
        # Score multiplier based on pack-years
        "threshold_high": 30,  # >30 pack-years = high risk
        "threshold_moderate": 15,
    },

    # Demographic factors
    "age": {
        "threshold_high": 65,
        "threshold_moderate": 50,
    },

    # Symptom weights - how much each symptom points toward each cancer type
    "symptoms": {
        "persistent_cough": {"adenocarcinoma": 0.08, "squamous_cell_carcinoma": 0.12, "small_cell_lung_cancer": 0.10, "large_cell_carcinoma": 0.08},
        "coughing_blood": {"squamous_cell_carcinoma": 0.20, "adenocarcinoma": 0.10, "small_cell_lung_cancer": 0.15, "large_cell_carcinoma": 0.12},
        "chest_pain": {"adenocarcinoma": 0.10, "squamous_cell_carcinoma": 0.10, "small_cell_lung_cancer": 0.12, "large_cell_carcinoma": 0.15},
        "shortness_of_breath": {"adenocarcinoma": 0.10, "squamous_cell_carcinoma": 0.12, "small_cell_lung_cancer": 0.08, "large_cell_carcinoma": 0.10},
        "unexplained_weight_loss": {"small_cell_lung_cancer": 0.18, "large_cell_carcinoma": 0.15, "squamous_cell_carcinoma": 0.10, "adenocarcinoma": 0.10},
        "fatigue": {"small_cell_lung_cancer": 0.10, "large_cell_carcinoma": 0.08, "adenocarcinoma": 0.06, "squamous_cell_carcinoma": 0.06},
        "hoarseness": {"squamous_cell_carcinoma": 0.12, "small_cell_lung_cancer": 0.10, "adenocarcinoma": 0.06, "large_cell_carcinoma": 0.06},
        "recurring_infections": {"squamous_cell_carcinoma": 0.10, "adenocarcinoma": 0.08, "large_cell_carcinoma": 0.08, "small_cell_lung_cancer": 0.05},
        "wheezing": {"squamous_cell_carcinoma": 0.10, "adenocarcinoma": 0.05, "small_cell_lung_cancer": 0.05, "large_cell_carcinoma": 0.05},
        "difficulty_swallowing": {"small_cell_lung_cancer": 0.12, "squamous_cell_carcinoma": 0.08, "large_cell_carcinoma": 0.06, "adenocarcinoma": 0.04},
        "finger_clubbing": {"adenocarcinoma": 0.12, "large_cell_carcinoma": 0.08, "squamous_cell_carcinoma": 0.04, "small_cell_lung_cancer": 0.02},
        "bone_pain": {"adenocarcinoma": 0.08, "small_cell_lung_cancer": 0.12, "large_cell_carcinoma": 0.10, "squamous_cell_carcinoma": 0.06}
    },

    # Exposure factors
    "exposures": {
        "asbestos": {"adenocarcinoma": 0.15, "squamous_cell_carcinoma": 0.10, "large_cell_carcinoma": 0.08, "small_cell_lung_cancer": 0.03},
        "radon": {"adenocarcinoma": 0.12, "squamous_cell_carcinoma": 0.10, "small_cell_lung_cancer": 0.08, "large_cell_carcinoma": 0.06},
        "air_pollution": {"adenocarcinoma": 0.10, "squamous_cell_carcinoma": 0.06, "large_cell_carcinoma": 0.05, "small_cell_lung_cancer": 0.03},
        "occupational_chemicals": {"adenocarcinoma": 0.08, "squamous_cell_carcinoma": 0.08, "large_cell_carcinoma": 0.06, "small_cell_lung_cancer": 0.04},
        "radiation_exposure": {"adenocarcinoma": 0.06, "squamous_cell_carcinoma": 0.06, "small_cell_lung_cancer": 0.05, "large_cell_carcinoma": 0.08}
    },

    # Medical history
    "medical_history": {
        "family_history_lung_cancer": {"adenocarcinoma": 0.15, "squamous_cell_carcinoma": 0.10, "small_cell_lung_cancer": 0.08, "large_cell_carcinoma": 0.08},
        "previous_cancer": {"adenocarcinoma": 0.08, "squamous_cell_carcinoma": 0.08, "small_cell_lung_cancer": 0.10, "large_cell_carcinoma": 0.08},
        "copd": {"squamous_cell_carcinoma": 0.15, "adenocarcinoma": 0.08, "small_cell_lung_cancer": 0.08, "large_cell_carcinoma": 0.06},
        "tuberculosis": {"adenocarcinoma": 0.10, "squamous_cell_carcinoma": 0.06, "large_cell_carcinoma": 0.04, "small_cell_lung_cancer": 0.02},
        "pulmonary_fibrosis": {"adenocarcinoma": 0.12, "squamous_cell_carcinoma": 0.06, "large_cell_carcinoma": 0.06, "small_cell_lung_cancer": 0.03}
    }
}


def calculate_risk(data):
    """
    Calculate lung cancer risk scores based on patient data.
    Returns prediction with confidence scores for each cancer type.
    """
    scores = {
        "adenocarcinoma": 0.0,
        "squamous_cell_carcinoma": 0.0,
        "small_cell_lung_cancer": 0.0,
        "large_cell_carcinoma": 0.0,
        "benign": 0.0
    }

    total_risk_factors = 0
    risk_factor_count = 0

    # 1. Smoking status
    smoking = data.get("smoking_status", "never")
    if smoking in RISK_WEIGHTS["smoking_status"]:
        for cancer_type, weight in RISK_WEIGHTS["smoking_status"][smoking].items():
            scores[cancer_type] += weight
        total_risk_factors += 1

    # 2. Pack-years (for current/former smokers)
    pack_years = data.get("pack_years", 0)
    if pack_years > 0:
        multiplier = 1.0
        if pack_years > RISK_WEIGHTS["pack_years"]["threshold_high"]:
            multiplier = 1.5
        elif pack_years > RISK_WEIGHTS["pack_years"]["threshold_moderate"]:
            multiplier = 1.2
        scores["squamous_cell_carcinoma"] *= multiplier
        scores["small_cell_lung_cancer"] *= multiplier
        total_risk_factors += 1

    # 3. Age
    age = data.get("age", 0)
    if age > RISK_WEIGHTS["age"]["threshold_high"]:
        age_boost = 0.10
    elif age > RISK_WEIGHTS["age"]["threshold_moderate"]:
        age_boost = 0.05
    else:
        age_boost = -0.05  # younger = lower risk, more likely benign
        scores["benign"] += 0.15
    for cancer_type in ["adenocarcinoma", "squamous_cell_carcinoma", "small_cell_lung_cancer", "large_cell_carcinoma"]:
        scores[cancer_type] += age_boost
    total_risk_factors += 1

    # 4. Gender
    gender = data.get("gender", "")
    if gender == "female":
        scores["adenocarcinoma"] += 0.05  # Adenocarcinoma more common in women
    elif gender == "male":
        scores["squamous_cell_carcinoma"] += 0.03
        scores["small_cell_lung_cancer"] += 0.02

    # 5. Symptoms
    symptoms = data.get("symptoms", [])
    for symptom in symptoms:
        if symptom in RISK_WEIGHTS["symptoms"]:
            for cancer_type, weight in RISK_WEIGHTS["symptoms"][symptom].items():
                scores[cancer_type] += weight
            risk_factor_count += 1

    # 6. Exposures
    exposures = data.get("exposures", [])
    for exposure in exposures:
        if exposure in RISK_WEIGHTS["exposures"]:
            for cancer_type, weight in RISK_WEIGHTS["exposures"][exposure].items():
                scores[cancer_type] += weight
            risk_factor_count += 1

    # 7. Medical history
    medical_history = data.get("medical_history", [])
    for condition in medical_history:
        if condition in RISK_WEIGHTS["medical_history"]:
            for cancer_type, weight in RISK_WEIGHTS["medical_history"][condition].items():
                scores[cancer_type] += weight
            risk_factor_count += 1

    # 8. Benign score adjustment
    # If few risk factors are present, benign is more likely
    if risk_factor_count < 2 and smoking == "never" and age < 50:
        scores["benign"] += 0.40
    elif risk_factor_count < 3:
        scores["benign"] += 0.15
    else:
        scores["benign"] += 0.02

    # Normalize to percentages
    total = sum(scores.values())
    if total > 0:
        for key in scores:
            scores[key] = round((scores[key] / total) * 100, 1)
    else:
        scores["benign"] = 100.0

    # Determine primary prediction
    primary = max(scores, key=scores.get)

    # Determine overall risk level
    cancer_risk = 100 - scores.get("benign", 0)
    if cancer_risk > 70:
        risk_level = "high"
    elif cancer_risk > 40:
        risk_level = "moderate"
    elif cancer_risk > 15:
        risk_level = "low"
    else:
        risk_level = "minimal"

    return {
        "prediction": primary,
        "scores": scores,
        "risk_level": risk_level,
        "cancer_risk_percentage": round(cancer_risk, 1),
        "risk_factors_detected": risk_factor_count,
        "cancer_info": CANCER_TYPES.get(primary, {})
    }
