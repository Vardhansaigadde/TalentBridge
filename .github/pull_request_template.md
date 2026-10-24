## 🌉 TalentBridge AI — Pull Request Submission

### 1. Contributor & Module Details
- **Team Member:** <!-- e.g., Member 2 -->
- **Assigned Module:** <!-- e.g., modules/fake_job_detection -->
- **Type of Change:**
  - [ ] 🚀 New algorithm / model implementation
  - [ ] 🎨 Streamlit UI enhancement in `interface.py`
  - [ ] 🧪 Unit tests addition in `tests/`
  - [ ] 📝 Documentation / README update
  - [ ] ⚙️ App registry update in `app.py`

---

### 2. Mandatory Architectural Checklist
> *You must check every item below before your PR can be merged.*

- [ ] **Strict Isolation:** I have **only** modified files inside my assigned `modules/<my_module>/` folder (or updated my line in `app.py`'s `MODULE_REGISTRY`). I have **not** modified other members' code.
- [ ] **Interface Contract:** My `interface.py` exposes a working `def render() -> None:` function.
- [ ] **No Large Files:** I did **not** commit large raw datasets (`.csv`, `.parquet`, `.xlsx`) or heavy binary weights (`.h5`, `.bin`, `.pt` > 50MB). Only `.gitkeep` files track empty folders.
- [ ] **No Secrets:** No API keys, passwords, database URIs, or personal credentials exist in my code.
- [ ] **All Tests Pass:** I ran `python -m pytest -v` locally and all 14+ platform integration and unit tests pass with zero errors.
- [ ] **Ethical Disclaimer:** My module UI includes the responsible AI disclaimer (`render_disclaimer()`).

---

### 3. Summary of Changes
<!-- Provide a concise description of what was implemented or modified. -->

---

### 4. Local Test Results
```bash
# Paste the final lines of your local pytest run here:
```
