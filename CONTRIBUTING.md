# 🤝 TalentBridge AI — Team Contribution & Governance Rules

Welcome to **TalentBridge AI**! This document defines the collaborative guidelines and repository rules designed to ensure that all 12 team members can develop their machine learning modules in parallel without disrupting the platform architecture or other members' work.

---

## 🏛️ The 5 Golden Rules of the Repository

### Rule 1: The "Module Sandbox" Policy (Zero Cross-Editing)
- You **only have write permission** to your assigned directory: `modules/<your_assigned_module>/`.
- **Never edit, refactor, or delete files inside another member's folder.**
- Platform core files (`app.py`, `shared/`, `requirements.txt`, `tests/`) are managed by the **Lead Architect (Member 1)**.

### Rule 2: Preserve the Interface Contract
The application dynamically loads your module. Your `modules/<your_module>/interface.py` file **MUST always export**:
```python
def render() -> None:
    """
    Renders Streamlit widgets and invokes model functions.
    Takes 0 arguments and returns None.
    """
    pass
```
Never change `render()` to take required arguments or rename it.

### Rule 3: Never Commit Large Datasets or Model Weights to Git
- Keep large datasets (`.csv`, `.parquet`, `.json`, `.xlsx`) in `modules/<your_module>/data/`.
- Keep heavy model weights (`.pt`, `.pkl`, `.h5` > 25MB) in `modules/<your_module>/artifacts/`.
- These extensions are filtered by [`.gitignore`](.gitignore). Use `.gitkeep` to keep folders tracked in git.
- If your trained model is small (e.g., standard scikit-learn TF-IDF / tree under 15MB), it may be serialized in `artifacts/`. For larger models, provide a script (`train.py` or `download_weights.py`).

### Rule 4: Never Commit Secrets, Passwords, or Personal Tokens
- Do not hardcode API keys (OpenAI, HuggingFace, AWS), passwords, or email credentials.
- Use environment variables (`.env` is ignored by Git) or pass mock test keys.

### Rule 5: Green Tests Before Every Pull Request
Before committing or creating a pull request, run:
```bash
python -m pytest -v
```
If any test fails, do **not** open the pull request until it is resolved.

---

## 🌿 Git Branching Strategy

To avoid merge conflicts, **direct pushes to the `main` branch are blocked**.

### 1. Branch Naming
Create a descriptive branch for your use case:
```bash
# Format: feature/member-<NUMBER>-<short-description>
git checkout -b feature/member-2-fake-job-classifier
```

### 2. Atomic Commits
Keep your commits scoped to your module:
```bash
git add modules/fake_job_detection/
git commit -m "feat(fake_job_detection): add preprocessing and logistic regression model"
```

### 3. Sync with Main Regularly
Before submitting your PR, rebase or merge from `main` to ensure you have the latest updates:
```bash
git fetch origin
git merge origin/main
```

---

## 📋 Pull Request (PR) Lifecycle

1. **Open PR:** Target `main` from your feature branch.
2. **Fill the Checklist:** GitHub will automatically show the PR template checklist. Confirm every item.
3. **Automated CI:** GitHub Actions will automatically run the full pytest test suite.
4. **Code Review:** The Lead Architect (Member 1) will review the PR for:
   - File scope (no modified files outside your folder).
   - Clean code and documentation.
   - Working Streamlit interface.
5. **Merge:** Merging uses **Squash and Merge** to keep the `main` git history clean and linear.

---

## 🆘 Troubleshooting Common Issues

### "My module raises an import error when loaded in Streamlit"
- Ensure your module doesn't rely on relative imports outside its package. Use `from shared.utils import render_disclaimer` or relative imports within your module (`from .model import MyModel`).

### "I need an external Python library"
- If your ML model requires a package not in `requirements.txt` (e.g. `xgboost`, `spacy`), discuss with **Member 1 (Lead)** before editing `requirements.txt` so dependencies remain lightweight and conflict-free.
