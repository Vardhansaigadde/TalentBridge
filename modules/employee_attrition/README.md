# Employee Attrition Prediction

**Assigned Lead:** Member 9  
**Module Identifier:** `modules.employee_attrition`  
**Status:** 🚧 In Development (Scaffold Ready)  

---

## 1. Module Overview
Forecasts employee turnover risk and isolates contributing workplace satisfaction factors.

This module operates independently within the TalentBridge AI platform. As **Member 9**, you own this directory and can develop, experiment, train models, and create tests without altering other members' code.

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
- Tenure, Department, and Compensation Level
- Overtime hours and Work-Life Balance survey scores
- Time since last promotion & Performance appraisal rating
- Stock option levels and manager relationship score

### Expected Outputs
- Attrition Risk Probability (0.0 to 1.0)
- Risk Tier: 'Low', 'Medium', 'Elevated'
- SHAP / LIME explanation of primary retention drivers

### Recommended ML Approaches
- `XGBoost with SHAP interpretability`
- `Random Forest Classifier`
- `Logistic Regression with L1 regularization`

---

## 4. Directory Structure
```
modules/employee_attrition/
├── __init__.py          # Exports render() and EmployeeAttritionPredictor
├── interface.py         # Streamlit UI contract
├── model.py             # Machine learning model class & pipeline
├── README.md            # This documentation
├── data/
│   └── .gitkeep         # Training data (ignored by git if large)
├── artifacts/
│   └── .gitkeep         # Serialized models (.pkl, .joblib, etc.)
└── tests/
    └── .gitkeep         # Unit tests (e.g., test_employee_attrition.py)
```

---

## 5. Next Steps for Member 9
1. **Branch Out:** Create your git feature branch: `git checkout -b feature/member-9-employee_attrition`.
2. **Collect Data:** Add your training data into `modules/employee_attrition/data/`.
3. **Build Pipeline:** Implement data preprocessing and ML training in `model.py` (or add a `train.py`).
4. **Save Artifacts:** Save your model weights into `artifacts/`.
5. **Connect UI:** Replace the scaffold in `interface.py` with custom Streamlit controls.
6. **Add Unit Tests:** Write test cases in `modules/employee_attrition/tests/test_employee_attrition.py`.
