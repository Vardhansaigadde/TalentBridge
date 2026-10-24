# AI Resume Analysis

**Assigned Lead:** Member 10  
**Module Identifier:** `modules.resume_analyzer`  
**Status:** 🚧 In Development (Scaffold Ready)  

---

## 1. Module Overview
Deep multi-dimensional resume parsing, structure scoring, action-verb density, and ATS readiness.

This module operates independently within the TalentBridge AI platform. As **Member 10**, you own this directory and can develop, experiment, train models, and create tests without altering other members' code.

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
- Resume Plain Text or Parsed Document
- Target Industry or Career Level (Entry, Mid, Executive)

### Expected Outputs
- Overall ATS Compatibility Score (0 - 100)
- Section-by-section breakdown (Experience, Skills, Education)
- Action verb strength, quantification score, and formatting checks

### Recommended ML Approaches
- `SpaCy Named Entity Recognition (NER)`
- `Regex Pattern Analyzers`
- `Pretrained Transformer Token Classifiers`

---

## 4. Directory Structure
```
modules/resume_analyzer/
├── __init__.py          # Exports render() and ResumeAnalyzer
├── interface.py         # Streamlit UI contract
├── model.py             # Machine learning model class & pipeline
├── README.md            # This documentation
├── data/
│   └── .gitkeep         # Training data (ignored by git if large)
├── artifacts/
│   └── .gitkeep         # Serialized models (.pkl, .joblib, etc.)
└── tests/
    └── .gitkeep         # Unit tests (e.g., test_resume_analyzer.py)
```

---

## 5. Next Steps for Member 10
1. **Branch Out:** Create your git feature branch: `git checkout -b feature/member-10-resume_analyzer`.
2. **Collect Data:** Add your training data into `modules/resume_analyzer/data/`.
3. **Build Pipeline:** Implement data preprocessing and ML training in `model.py` (or add a `train.py`).
4. **Save Artifacts:** Save your model weights into `artifacts/`.
5. **Connect UI:** Replace the scaffold in `interface.py` with custom Streamlit controls.
6. **Add Unit Tests:** Write test cases in `modules/resume_analyzer/tests/test_resume_analyzer.py`.
