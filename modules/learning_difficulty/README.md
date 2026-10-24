# Personalized Learning Difficulty Detection

**Assigned Lead:** Member 7  
**Module Identifier:** `modules.learning_difficulty`  
**Status:** 🚧 In Development (Scaffold Ready)  

---

## 1. Module Overview
Detects real-time student struggle or learning barriers during course modules and quizzes.

This module operates independently within the TalentBridge AI platform. As **Member 7**, you own this directory and can develop, experiment, train models, and create tests without altering other members' code.

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
- Time spent per quiz question & Video replay counts
- Incorrect attempt sequences and retry frequency
- Hint-usage patterns and module dropout timestamps

### Expected Outputs
- Struggle Index: 'Mastered', 'Mild Friction', 'High Difficulty'
- Specific bottleneck concepts flagged
- Adaptive pedagogical remediation recommendation

### Recommended ML Approaches
- `Long Short-Term Memory (LSTM) Networks`
- `Hidden Markov Models (HMM)`
- `Isolation Forest (Anomaly Detection)`

---

## 4. Directory Structure
```
modules/learning_difficulty/
├── __init__.py          # Exports render() and LearningDifficultyDetector
├── interface.py         # Streamlit UI contract
├── model.py             # Machine learning model class & pipeline
├── README.md            # This documentation
├── data/
│   └── .gitkeep         # Training data (ignored by git if large)
├── artifacts/
│   └── .gitkeep         # Serialized models (.pkl, .joblib, etc.)
└── tests/
    └── .gitkeep         # Unit tests (e.g., test_learning_difficulty.py)
```

---

## 5. Next Steps for Member 7
1. **Branch Out:** Create your git feature branch: `git checkout -b feature/member-7-learning_difficulty`.
2. **Collect Data:** Add your training data into `modules/learning_difficulty/data/`.
3. **Build Pipeline:** Implement data preprocessing and ML training in `model.py` (or add a `train.py`).
4. **Save Artifacts:** Save your model weights into `artifacts/`.
5. **Connect UI:** Replace the scaffold in `interface.py` with custom Streamlit controls.
6. **Add Unit Tests:** Write test cases in `modules/learning_difficulty/tests/test_learning_difficulty.py`.
