# Student Performance Prediction

**Assigned Lead:** Member 3  
**Module Identifier:** `modules.student_performance`  
**Status:** 🚧 In Development (Scaffold Ready)  

---

## 1. Module Overview
Predicts academic outcomes, GPA trends, and graduation risk based on historical learning metrics.

This module operates independently within the TalentBridge AI platform. As **Member 3**, you own this directory and can develop, experiment, train models, and create tests without altering other members' code.

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
- Past Semester GPAs & Course Grades
- Attendance rate and LMS portal engagement
- Assignment submission punctuality
- Extracurricular participation index

### Expected Outputs
- Predicted End-of-Semester GPA / Grade band
- Risk Classification: 'On-Track' vs 'At-Risk'
- Key academic factor influence weights

### Recommended ML Approaches
- `Ridge / Lasso Regression`
- `Gradient Boosting Regressor`
- `LightGBM`
- `Random Forest Regressor`

---

## 4. Directory Structure
```
modules/student_performance/
├── __init__.py          # Exports render() and StudentPerformancePredictor
├── interface.py         # Streamlit UI contract
├── model.py             # Machine learning model class & pipeline
├── README.md            # This documentation
├── data/
│   └── .gitkeep         # Training data (ignored by git if large)
├── artifacts/
│   └── .gitkeep         # Serialized models (.pkl, .joblib, etc.)
└── tests/
    └── .gitkeep         # Unit tests (e.g., test_student_performance.py)
```

---

## 5. Next Steps for Member 3
1. **Branch Out:** Create your git feature branch: `git checkout -b feature/member-3-student_performance`.
2. **Collect Data:** Add your training data into `modules/student_performance/data/`.
3. **Build Pipeline:** Implement data preprocessing and ML training in `model.py` (or add a `train.py`).
4. **Save Artifacts:** Save your model weights into `artifacts/`.
5. **Connect UI:** Replace the scaffold in `interface.py` with custom Streamlit controls.
6. **Add Unit Tests:** Write test cases in `modules/student_performance/tests/test_student_performance.py`.
