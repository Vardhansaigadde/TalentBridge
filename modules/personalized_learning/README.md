# Personalized Learning Recommendations

**Assigned Lead:** Member 12  
**Module Identifier:** `modules.personalized_learning`  
**Status:** 🚧 In Development (Scaffold Ready)  

---

## 1. Module Overview
Recommends tailored courses, learning paths, and skill drills to close individual career gaps.

This module operates independently within the TalentBridge AI platform. As **Member 12**, you own this directory and can develop, experiment, train models, and create tests without altering other members' code.

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
- Learner Target Career Goal & Current Skill Inventory
- Past completed course ratings and preferred learning style
- Available study hours per week

### Expected Outputs
- Top-N Recommended Learning Modules / Courses
- Curated Learning Pathway Sequence
- Predicted Skill Growth trajectory

### Recommended ML Approaches
- `Collaborative Filtering (Matrix Factorization / SVD)`
- `Content-Based Cosine Filtering`
- `Graph-Based Knowledge Tracing`

---

## 4. Directory Structure
```
modules/personalized_learning/
├── __init__.py          # Exports render() and PersonalizedLearningRecommender
├── interface.py         # Streamlit UI contract
├── model.py             # Machine learning model class & pipeline
├── README.md            # This documentation
├── data/
│   └── .gitkeep         # Training data (ignored by git if large)
├── artifacts/
│   └── .gitkeep         # Serialized models (.pkl, .joblib, etc.)
└── tests/
    └── .gitkeep         # Unit tests (e.g., test_personalized_learning.py)
```

---

## 5. Next Steps for Member 12
1. **Branch Out:** Create your git feature branch: `git checkout -b feature/member-12-personalized_learning`.
2. **Collect Data:** Add your training data into `modules/personalized_learning/data/`.
3. **Build Pipeline:** Implement data preprocessing and ML training in `model.py` (or add a `train.py`).
4. **Save Artifacts:** Save your model weights into `artifacts/`.
5. **Connect UI:** Replace the scaffold in `interface.py` with custom Streamlit controls.
6. **Add Unit Tests:** Write test cases in `modules/personalized_learning/tests/test_personalized_learning.py`.
