# AI Interview Performance Analysis and Feedback

**Assigned Lead:** Member 6  
**Module Identifier:** `modules.interview_analyzer`  
**Status:** 🚧 In Development (Scaffold Ready)  

---

## 1. Module Overview
Evaluates candidate video/audio/transcript interview responses to provide actionable feedback.

This module operates independently within the TalentBridge AI platform. As **Member 6**, you own this directory and can develop, experiment, train models, and create tests without altering other members' code.

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
- Interview Response Audio / Video or Transcript Text
- Job Role & Technical Question prompts
- Speech pace, filler word frequency, and sentiment metrics

### Expected Outputs
- Response Quality & Relevance Score (1 - 10)
- Clarity, Confidence, and Structure Evaluation
- Specific improvement tips (STAR method alignment, filler word reduction)

### Recommended ML Approaches
- `Whisper ASR + LLM Prompt Evaluation`
- `BERT Sentiment & Content Relevance`
- `Prosodic Speech Feature Analysis`

---

## 4. Directory Structure
```
modules/interview_analyzer/
├── __init__.py          # Exports render() and InterviewAnalyzer
├── interface.py         # Streamlit UI contract
├── model.py             # Machine learning model class & pipeline
├── README.md            # This documentation
├── data/
│   └── .gitkeep         # Training data (ignored by git if large)
├── artifacts/
│   └── .gitkeep         # Serialized models (.pkl, .joblib, etc.)
└── tests/
    └── .gitkeep         # Unit tests (e.g., test_interview_analyzer.py)
```

---

## 5. Next Steps for Member 6
1. **Branch Out:** Create your git feature branch: `git checkout -b feature/member-6-interview_analyzer`.
2. **Collect Data:** Add your training data into `modules/interview_analyzer/data/`.
3. **Build Pipeline:** Implement data preprocessing and ML training in `model.py` (or add a `train.py`).
4. **Save Artifacts:** Save your model weights into `artifacts/`.
5. **Connect UI:** Replace the scaffold in `interface.py` with custom Streamlit controls.
6. **Add Unit Tests:** Write test cases in `modules/interview_analyzer/tests/test_interview_analyzer.py`.
