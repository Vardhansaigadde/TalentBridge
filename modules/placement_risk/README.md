# Student Placement Risk Prediction

**Assigned Lead:** Member 5  
**Module Identifier:** `modules.placement_risk`  
**Status:** 🚧 In Development (Scaffold Ready)  

---

## 1. Module Overview
Early identification of graduating students at risk of not securing campus placements.

This module operates independently within the TalentBridge AI platform. As **Member 5**, you own this directory and can develop, experiment, train models, and create tests without altering other members' code.

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
- Cumulative CGPA and Backlog History
- Technical assessment & Coding test scores
- Internship completion and project count
- Communication & Soft skills evaluation score

### Expected Outputs
- Placement Risk Category: 'Low Risk', 'Moderate Risk', 'Critical Risk'
- Probability of placement within 6 months
- Recommended intervention pathways (e.g. coding bootcamp, resume revamping)

### Recommended ML Approaches
- `Random Forest Classifier`
- `XGBoost Classifier`
- `Balanced Random Forest (Imbalanced Data)`

---

## 4. Directory Structure
```
modules/placement_risk/
├── __init__.py          # Exports render() and PlacementRiskClassifier
├── interface.py         # Streamlit UI contract
├── model.py             # Machine learning model class & pipeline
├── README.md            # This documentation
├── data/
│   └── .gitkeep         # Training data (ignored by git if large)
├── artifacts/
│   └── .gitkeep         # Serialized models (.pkl, .joblib, etc.)
└── tests/
    └── .gitkeep         # Unit tests (e.g., test_placement_risk.py)
```

---

## 5. Next Steps for Member 5
1. **Branch Out:** Create your git feature branch: `git checkout -b feature/member-5-placement_risk`.
2. **Collect Data:** Add your training data into `modules/placement_risk/data/`.
3. **Build Pipeline:** Implement data preprocessing and ML training in `model.py` (or add a `train.py`).
4. **Save Artifacts:** Save your model weights into `artifacts/`.
5. **Connect UI:** Replace the scaffold in `interface.py` with custom Streamlit controls.
6. **Add Unit Tests:** Write test cases in `modules/placement_risk/tests/test_placement_risk.py`.
