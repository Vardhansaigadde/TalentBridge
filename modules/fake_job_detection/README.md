# Fake Job Posting Detection

**Assigned Lead:** Member 2  
**Module Identifier:** `modules.fake_job_detection`  
**Status:** 🚧 In Development (Scaffold Ready)  

---

## 1. Module Overview
Classifies online job postings as legitimate or fraudulent using NLP classification.

This module operates independently within the TalentBridge AI platform. As **Member 2**, you own this directory and can develop, experiment, train models, and create tests without altering other members' code.

---

## 2. Interface Contract
TalentBridge AI dynamically loads this module via the `render()` function in `interface.py`:

```python
def render() -> None:
    # Build your Streamlit UI components here
    # Call your trained model from model.py
    pass
```

---

## 3. Specifications & Architecture

### Expected Inputs
- Job Title & Company Profile
- Job Description & Requirements text
- Telecommuting & Employment Type flags
- Company Logo presence & screening questions

### Expected Outputs
- Fraud Probability Score (0.0 to 1.0)
- Classification Label: 'Legitimate' vs 'Fraudulent'
- Risk Indicator flags (e.g., suspicious contact domain, vague requirements)

### Recommended ML Approaches
- `Logistic Regression with TF-IDF`
- `Random Forest Classifier`
- `XGBoost`
- `RoBERTa / DistilBERT`

---

## 4. Directory Structure
```
modules/fake_job_detection/
├── __init__.py          # Exports render() and FakeJobDetector
├── interface.py         # Streamlit UI contract
├── model.py             # Machine learning model class & pipeline
├── README.md            # This documentation
├── data/
│   └── .gitkeep         # Training data (ignored by git if large)
├── artifacts/
│   └── .gitkeep         # Serialized models (.pkl, .joblib, etc.)
└── tests/
    └── .gitkeep         # Unit tests (e.g., test_fake_job_detection.py)
```

---

## 5. Next Steps for Member 2
1. **Branch Out:** Create your git feature branch: `git checkout -b feature/member-2-fake_job_detection`.
2. **Collect Data:** Add your training data into `modules/fake_job_detection/data/`.
3. **Build Pipeline:** Implement data preprocessing and ML training in `model.py` (or add a `train.py`).
4. **Save Artifacts:** Save your model weights into `artifacts/`.
5. **Connect UI:** Replace the scaffold in `interface.py` with custom Streamlit controls.
6. **Add Unit Tests:** Write test cases in `modules/fake_job_detection/tests/test_fake_job_detection.py`.
