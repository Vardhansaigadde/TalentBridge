# 🌉 TalentBridge AI — Integrated Machine Learning Platform

> A modular, 12-member machine learning and talent intelligence platform unifying predictive analytics, NLP, and career recommendation systems into a single enterprise-ready application.

[![Python Version](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.14-blue.svg)](https://www.python.org/)
[![UI Framework](https://img.shields.io/badge/UI-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![ML Library](https://img.shields.io/badge/ML-Scikit--Learn-F7931E.svg)](https://scikit-learn.org/)
[![Test Suite](https://img.shields.io/badge/Tests-Pytest%20Passing-brightgreen.svg)](https://pytest.org/)

---

## 1. Project Overview & Mission

**TalentBridge AI** integrates 12 distinct machine learning applications across the talent acquisition, student career development, and workforce retention lifecycles. 

The platform is designed around **strict modular architecture** allowing 12 developers to build, train, evaluate, and test their machine learning models independently in isolation, without blocking each other or causing git merge conflicts.

---

## 2. Team Member Assignments & Use Case Matrix

| # | Module Directory | Use Case Name | Assigned Lead | Implementation Status |
|---|------------------|---------------|---------------|-----------------------|
| 1 | `modules/resume_job_matching/` | **Resume–Job Matching** | **Member 1 (Lead)** | ✅ **Active Baseline Implemented** |
| 2 | `modules/fake_job_detection/` | Fake Job Posting Detection | Member 2 | 🚧 In Development (Scaffold Ready) |
| 3 | `modules/student_performance/` | Student Performance Prediction | Member 3 | 🚧 In Development (Scaffold Ready) |
| 4 | `modules/entrance_exam_prediction/` | Entrance Examination Performance Prediction | Member 4 | 🚧 In Development (Scaffold Ready) |
| 5 | `modules/placement_risk/` | Student Placement Risk Prediction | Member 5 | 🚧 In Development (Scaffold Ready) |
| 6 | `modules/interview_analyzer/` | AI Interview Performance Analysis & Feedback | Member 6 | 🚧 In Development (Scaffold Ready) |
| 7 | `modules/learning_difficulty/` | Personalized Learning Difficulty Detection | Member 7 | 🚧 In Development (Scaffold Ready) |
| 8 | `modules/fairness_recruitment/` | Fairness-Aware Recruitment | Member 8 | 🚧 In Development (Scaffold Ready) |
| 9 | `modules/employee_attrition/` | Employee Attrition Prediction | Member 9 | 🚧 In Development (Scaffold Ready) |
| 10 | `modules/resume_analyzer/` | AI Resume Analysis | Member 10 | 🚧 In Development (Scaffold Ready) |
| 11 | `modules/internship_fraud_detection/` | Fake Internship Detection | Member 11 | 🚧 In Development (Scaffold Ready) |
| 12 | `modules/personalized_learning/` | Personalized Learning Recommendations | Member 12 | 🚧 In Development (Scaffold Ready) |

---

## 3. Project Directory Structure

```
TalentBridge-AI/
├── app.py                     # Central Streamlit entry point & lazy module loader
├── requirements.txt           # Minimal core project dependencies
├── README.md                  # Root architectural & team collaboration documentation
├── .gitignore                 # Excludes models, venv, datasets, caches, IDE files
├── modules/
│   ├── __init__.py            # Root modules package
│   ├── resume_job_matching/   # [MEMBER 1] Full working baseline
│   │   ├── __init__.py        # Exports interface and matcher
│   │   ├── interface.py       # Streamlit UI with sample prefill and metrics
│   │   ├── model.py           # TF-IDF & Cosine Similarity inference engine
│   │   ├── preprocessing.py   # Text normalization and skill gap extraction
│   │   ├── train.py           # Vectorizer training & artifact serialization
│   │   ├── config.py          # Sample profiles, thresholds, and paths
│   │   ├── README.md          # Member 1 technical specifications
│   │   ├── data/
│   │   │   └── .gitkeep       # Datasets folder (git-tracked)
│   │   ├── artifacts/
│   │   │   ├── .gitkeep       # Model weights folder
│   │   │   └── tfidf_vectorizer.joblib  # Serialized vectorizer
│   │   └── tests/
│   │       └── test_resume_job_matching.py # Pytest unit tests
│   │
│   │── fake_job_detection/          # [MEMBER 2]  (__init__, interface, model, README, data, artifacts, tests)
│   │── student_performance/         # [MEMBER 3]  (__init__, interface, model, README, data, artifacts, tests)
│   │── entrance_exam_prediction/    # [MEMBER 4]  (__init__, interface, model, README, data, artifacts, tests)
│   │── placement_risk/              # [MEMBER 5]  (__init__, interface, model, README, data, artifacts, tests)
│   │── interview_analyzer/          # [MEMBER 6]  (__init__, interface, model, README, data, artifacts, tests)
│   │── learning_difficulty/         # [MEMBER 7]  (__init__, interface, model, README, data, artifacts, tests)
│   │── fairness_recruitment/        # [MEMBER 8]  (__init__, interface, model, README, data, artifacts, tests)
│   │── employee_attrition/          # [MEMBER 9]  (__init__, interface, model, README, data, artifacts, tests)
│   │── resume_analyzer/             # [MEMBER 10] (__init__, interface, model, README, data, artifacts, tests)
│   │── internship_fraud_detection/  # [MEMBER 11] (__init__, interface, model, README, data, artifacts, tests)
│   └── personalized_learning/       # [MEMBER 12] (__init__, interface, model, README, data, artifacts, tests)
│
├── shared/
│   ├── __init__.py            # Shared utility exports
│   └── utils.py               # Headers, ethical disclaimers, placeholder scaffolders
├── tests/
│   └── test_module_integration.py # Platform-wide contract & registry verification tests
└── data/
    └── .gitkeep               # Root shared data directory (optional)
```

---

## 4. Getting Started & Installation

### Prerequisites
- Python 3.10+ (tested through 3.14)
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/WHENKEY2007/TalentBridge.git
cd TalentBridge
```

### 2. Create and Activate a Virtual Environment
**On Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**On macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`. Use the sidebar to navigate between all 12 modules.

---

## 5. Module Interface Contract

Every team member must adhere to the **`render()` contract** in `modules/<your_module>/interface.py`:

```python
"""
File: modules/<your_module_name>/interface.py
"""

def render() -> None:
    """
    Entry point invoked dynamically by app.py when the user selects this module.
    Renders Streamlit controls, processes input, and presents model predictions.
    """
    # 1. Display module UI elements
    # 2. Collect user inputs (text, sliders, file upload)
    # 3. Call your model from model.py
    # 4. Display charts, metrics, and ethical disclaimers
    pass
```

### Lazy Loading Architecture
To maintain sub-second application startup, `app.py` **does not load model weights into memory at boot**. When a user selects a module from the sidebar, `app.py` dynamically imports `modules.<your_module>.interface` and invokes `render()`. 

If an unhandled exception or missing library occurs inside a module, `app.py` catches it gracefully and presents diagnostic information without crashing the entire platform.

---

## 6. Guide for Team Members (How to Work in Your Module)

### Rule 1: Strict Directory Isolation
Each member works **only** within their designated directory under `modules/<your_assigned_module>/`. Do not edit code, models, or configurations inside other members' directories.

### Rule 2: Step-by-Step Implementation Workflow
1. **Switch to your assigned directory:**
   ```bash
   cd modules/<your_module_name>/
   ```
2. **Add training data:**
   Place datasets into `data/`. Note that large data files (`.csv`, `.parquet`, etc.) are ignored by git via `.gitignore`, while the folder is preserved by `.gitkeep`.
3. **Build your ML Model:**
   Implement preprocessing and feature transformations. Train your algorithm in `model.py` (or create a `train.py` script) and serialize trained checkpoints into `artifacts/`.
4. **Implement your UI:**
   In `interface.py`, replace the `render_placeholder()` call with your interactive Streamlit widgets and inference output presentation.
5. **Add Unit Tests:**
   Write unit tests inside `tests/test_<your_module_name>.py`.
6. **Update Documentation:**
   Update your module's `README.md` with dataset sources, performance metrics (Accuracy, F1, RMSE), and limitations.

---

## 7. Git Branching & Pull Request Workflow

To maintain repository stability across 12 contributors:

### Branch Naming Convention
Create a branch named after your member number and module:
```bash
git checkout -b feature/member-2-fake-job-detection
```

### Commit Guidelines
Make focused commits affecting only your module:
```bash
git add modules/fake_job_detection/
git commit -m "feat(fake_job_detection): add text preprocessing and TF-IDF pipeline"
```

### Pre-PR Verification
Before opening a Pull Request, always verify that all platform integration tests pass:
```bash
python -m pytest -v
```

### Pull Request Checklist
- [ ] Only files inside `modules/<your_module>/` or your entry in `MODULE_REGISTRY` were modified.
- [ ] `modules/<your_module>/interface.py` exposes a working `render()` function.
- [ ] No hardcoded API keys, passwords, or personal credentials exist in code.
- [ ] Unit tests pass: `python -m pytest -v`.
- [ ] Module `README.md` is updated with input/output details.

---

## 8. Updating the Module Navigation Registry

The navigation registry in `app.py` maps sidebar items to module paths. When you transition your module from development to production, update its registry entry in `app.py`:

```python
# In app.py -> MODULE_REGISTRY
{
    "id": "fake_job_detection",
    "title": "Fake Job Posting Detection",
    "member": "Member 2",
    "category": "Trust & Safety",
    "icon": "🛡️",
    "module_path": "modules.fake_job_detection.interface",
    "status": "Production Baseline",       # <-- Update status
    "badge_color": "#22c55e",              # <-- Green badge
    "description": "NLP classifier detecting fraudulent recruitment postings and scam signals.",
}
```

---

## 9. Ethical AI & Responsible Machine Learning

All predictive components within TalentBridge AI must adhere to the following principles:

1. **Non-Deterministic Decisions:** Machine learning outputs are analytical decision-support tools. A similarity score or placement probability is **not** a deterministic decision or hiring guarantee.
2. **Fairness & Bias Auditing:** Every model must be audited for disparate impact across protected classes (gender, ethnicity, age) using Member 8's `fairness_recruitment` toolkit.
3. **Transparency & Explainability:** Whenever feasible, provide interpretable factors (e.g. matched/missing skills, feature importances, SHAP values) rather than opaque black-box scores.
4. **Clear User Disclaimers:** All module interfaces must include an ethical guidance notice using `shared.utils.render_disclaimer()`.

---

## 10. Running the Test Suite

Run all unit tests across modules and integration tests:
```bash
python -m pytest -v
```

To run tests for a specific module:
```bash
python -m pytest modules/resume_job_matching/tests/ -v
```
