# Fairness-Aware Recruitment

**Assigned Lead:** Member 8  
**Module Identifier:** `modules.fairness_recruitment`  
**Status:** 🚧 In Development (Scaffold Ready)  

---

## 1. Module Overview
Audits candidate screening pipelines for demographic parity, disparate impact, and algorithmic bias.

This module operates independently within the TalentBridge AI platform. As **Member 8**, you own this directory and can develop, experiment, train models, and create tests without altering other members' code.

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
- Recruitment decisions / candidate selection labels
- Protected attribute annotations (Gender, Ethnicity, Age group)
- Candidate qualification features and test scores

### Expected Outputs
- Disparate Impact Ratio (4/5th Rule Compliance)
- Statistical Parity Difference & Equal Opportunity Difference
- Bias Mitigation / Re-weighting recommendations (AIF360 / Fairlearn)

### Recommended ML Approaches
- `Fairlearn Adversarial Debiasing`
- `Reweighting Preprocessing`
- `Equalized Odds Post-processing`

---

## 4. Directory Structure
```
modules/fairness_recruitment/
├── __init__.py          # Exports render() and FairnessAuditor
├── interface.py         # Streamlit UI contract
├── model.py             # Machine learning model class & pipeline
├── README.md            # This documentation
├── data/
│   └── .gitkeep         # Training data (ignored by git if large)
├── artifacts/
│   └── .gitkeep         # Serialized models (.pkl, .joblib, etc.)
└── tests/
    └── .gitkeep         # Unit tests (e.g., test_fairness_recruitment.py)
```

---

## 5. Next Steps for Member 8
1. **Branch Out:** Create your git feature branch: `git checkout -b feature/member-8-fairness_recruitment`.
2. **Collect Data:** Add your training data into `modules/fairness_recruitment/data/`.
3. **Build Pipeline:** Implement data preprocessing and ML training in `model.py` (or add a `train.py`).
4. **Save Artifacts:** Save your model weights into `artifacts/`.
5. **Connect UI:** Replace the scaffold in `interface.py` with custom Streamlit controls.
6. **Add Unit Tests:** Write test cases in `modules/fairness_recruitment/tests/test_fairness_recruitment.py`.
