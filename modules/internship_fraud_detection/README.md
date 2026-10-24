# Fake Internship Detection

**Assigned Lead:** Member 11  
**Module Identifier:** `modules.internship_fraud_detection`  
**Status:** 🚧 In Development (Scaffold Ready)  

---

## 1. Module Overview
Protects student job-seekers from predatory, unpaid fee-charging, or fraudulent internship listings.

This module operates independently within the TalentBridge AI platform. As **Member 11**, you own this directory and can develop, experiment, train models, and create tests without altering other members' code.

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
- Internship Title, Stipend details, and Company registration
- Application requirements (e.g. upfront security deposits requested)
- Domain verification & Contact information

### Expected Outputs
- Scam Risk Probability (0.0 to 1.0)
- Risk Level: 'Verified Safe' vs 'Suspicious' vs 'High Scam Threat'
- Detected Red Flags (e.g. 'Demands registration fee', 'Unregistered domain')

### Recommended ML Approaches
- `TF-IDF + Naive Bayes / SVM`
- `Ensemble Tree Classifiers`
- `Rule-based Red Flag Scoring Engine`

---

## 4. Directory Structure
```
modules/internship_fraud_detection/
├── __init__.py          # Exports render() and InternshipFraudDetector
├── interface.py         # Streamlit UI contract
├── model.py             # Machine learning model class & pipeline
├── README.md            # This documentation
├── data/
│   └── .gitkeep         # Training data (ignored by git if large)
├── artifacts/
│   └── .gitkeep         # Serialized models (.pkl, .joblib, etc.)
└── tests/
    └── .gitkeep         # Unit tests (e.g., test_internship_fraud_detection.py)
```

---

## 5. Next Steps for Member 11
1. **Branch Out:** Create your git feature branch: `git checkout -b feature/member-11-internship_fraud_detection`.
2. **Collect Data:** Add your training data into `modules/internship_fraud_detection/data/`.
3. **Build Pipeline:** Implement data preprocessing and ML training in `model.py` (or add a `train.py`).
4. **Save Artifacts:** Save your model weights into `artifacts/`.
5. **Connect UI:** Replace the scaffold in `interface.py` with custom Streamlit controls.
6. **Add Unit Tests:** Write test cases in `modules/internship_fraud_detection/tests/test_internship_fraud_detection.py`.
