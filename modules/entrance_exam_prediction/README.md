# Entrance Examination Performance Prediction

**Assigned Lead:** Member 4  
**Module Identifier:** `modules.entrance_exam_prediction`  
**Status:** 🚧 In Development (Scaffold Ready)  

---

## 1. Module Overview
Estimates admission examination percentile and university qualification likelihood.

This module operates independently within the TalentBridge AI platform. As **Member 4**, you own this directory and can develop, experiment, train models, and create tests without altering other members' code.

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
- Mock Exam Scores across Subject Modules (Math, Logic, Verbal)
- Preparation time (hours/week) & Study resources utilized
- Undergraduate / High School academic baseline
- Test-taking frequency and pacing metrics

### Expected Outputs
- Predicted Percentile Rank (0 - 100th)
- Estimated Composite Score Range
- Target University Admission Feasibility (Safe / Target / Reach)

### Recommended ML Approaches
- `Support Vector Regression (SVR)`
- `CatBoost Regressor`
- `Neural Multi-Layer Perceptron (MLP)`

---

## 4. Directory Structure
```
modules/entrance_exam_prediction/
├── __init__.py          # Exports render() and EntranceExamPredictor
├── interface.py         # Streamlit UI contract
├── model.py             # Machine learning model class & pipeline
├── README.md            # This documentation
├── data/
│   └── .gitkeep         # Training data (ignored by git if large)
├── artifacts/
│   └── .gitkeep         # Serialized models (.pkl, .joblib, etc.)
└── tests/
    └── .gitkeep         # Unit tests (e.g., test_entrance_exam_prediction.py)
```

---

## 5. Next Steps for Member 4
1. **Branch Out:** Create your git feature branch: `git checkout -b feature/member-4-entrance_exam_prediction`.
2. **Collect Data:** Add your training data into `modules/entrance_exam_prediction/data/`.
3. **Build Pipeline:** Implement data preprocessing and ML training in `model.py` (or add a `train.py`).
4. **Save Artifacts:** Save your model weights into `artifacts/`.
5. **Connect UI:** Replace the scaffold in `interface.py` with custom Streamlit controls.
6. **Add Unit Tests:** Write test cases in `modules/entrance_exam_prediction/tests/test_entrance_exam_prediction.py`.
