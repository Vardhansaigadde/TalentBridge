# Module 1: Resume–Job Matching Engine

**Assigned Lead:** Member 1 (Lead Architect)  
**Status:** ✅ Production Hybrid Engine Implemented  
**Package:** `modules.resume_job_matching`

---

## 1. Overview & Objective

The **Resume–Job Matching Engine** provides multi-dimensional candidate-to-job compatibility analysis. It accepts multi-format resume documents (**PDF, DOCX, TXT**), evaluates domain skills taxonomy coverage across 6 technical disciplines, computes vocabulary overlap using TF-IDF and Cosine distance, and delivers an Applicant Tracking System (ATS) structural audit with a prioritized optimization plan.

---

## 2. Machine Learning & NLP Architecture

### A. Document Parsing Pipeline (`preprocessing.py`)
- **PDF Extraction:** Uses `PyMuPDF` (`fitz`) to extract text streams across all document pages.
- **DOCX Extraction:** Parses paragraph runs and table cell matrices using `python-docx`.
- **Text Normalization:** Lowercasing, URL/email stripping, punctuation normalization while preserving domain tokens (`c++`, `c#`, `ci/cd`, `rest api`).

### B. Curated Skills Taxonomy
Scans resumes and job descriptions against categorized technical competencies:
1. **Programming Languages:** Python, Java, C++, C#, JavaScript, TypeScript, Go, Rust, SQL, Bash, etc.
2. **Frameworks & Web:** FastAPI, Django, Flask, React, Next.js, Node.js, Spring Boot, GraphQL, REST API, etc.
3. **Cloud & DevOps:** AWS, Azure, GCP, Docker, Kubernetes, Terraform, CI/CD, GitHub Actions, Helm, Linux, etc.
4. **Databases & Storage:** PostgreSQL, MySQL, MongoDB, Redis, Cassandra, Elasticsearch, DynamoDB, etc.
5. **Data & AI/ML:** PyTorch, TensorFlow, Scikit-learn, Pandas, NumPy, NLP, LLMs, Computer Vision, etc.
6. **Architecture & Methods:** Microservices, System Design, Distributed Systems, Agile, Scrum, JIRA, etc.

### C. Hybrid Composite Scoring Formulation (`model.py`)
Rather than relying purely on bag-of-words or uncalibrated word frequencies, the engine uses a weighted composite metric:

$$\text{Composite Score} = 0.55 \times S_{\text{skills}} + 0.45 \times S_{\text{tfidf}}$$

Where:
- **$S_{\text{skills}}$ (Skills Coverage Ratio):**
  $$S_{\text{skills}} = \frac{|\text{Skills}_{\text{Job}} \cap \text{Skills}_{\text{Resume}}|}{|\text{Skills}_{\text{Job}}|}$$
- **$S_{\text{tfidf}}$ (Cosine Distance):**
  $$S_{\text{tfidf}} = \frac{u_{\text{resume}} \cdot v_{\text{job}}}{\|u_{\text{resume}}\|_2 \|v_{\text{job}}\|_2}$$

### D. Classification Tiers
- **High Match:** $\ge 75\%$
- **Moderate Match:** $45\% - 74\%$
- **Low Match:** $< 45\%$

### E. ATS Structural & Impact Audit
- **Length Analysis:** Assesses optimal word counts (250–850 words).
- **Section Verification:** Verifies standard headers (*Contact Info, Experience, Education, Skills, Projects*).
- **Action Verb Density:** Identifies power verbs (*Architected, Engineered, Optimized, Automated*).
- **Quantification Metric:** Detects numerical achievements, percentages, and scale indicators.
- **Action Plan:** Automatically generates numbered recommendations for candidates.

---

## 3. Inputs & Outputs Contract

### Expected Inputs
- **Resume:** Uploaded file (`.pdf`, `.docx`, `.txt`) or pasted plain text.
- **Job Description:** Selected preset or pasted job posting.

### Expected Outputs
- `match_percentage`: Weighted composite alignment percentage.
- `skills_overlap_percentage`: Domain technical skills coverage.
- `textual_similarity_percentage`: TF-IDF vocabulary similarity.
- `category_breakdown`: Category-by-category skill matrix.
- `matched_keywords` & `missing_keywords`: Specific competencies found and missing.
- `ats_audit`: Structural health metrics and section status.
- `optimization_plan`: Prioritized action items to boost match rate.

---

## 4. Ethical AI & Critical Disclaimer

> ⚠️ **NOTICE: Text-similarity is NOT a hiring guarantee or employment probability.**
> Machine learning similarity scores evaluate textual and competency overlap with a specific job posting. Real-world talent evaluation necessitates holistic human assessment of problem solving, cultural contribution, interpersonal communication, and live code reviews.

---

## 5. File Layout

```
modules/resume_job_matching/
├── __init__.py           # Exports public API and render()
├── config.py             # Hyperparameters, skills taxonomy, and presets
├── preprocessing.py      # PDF/DOCX parsing, taxonomy extraction, ATS audit
├── model.py              # Hybrid ResumeJobMatcher implementation
├── train.py              # Vectorizer training & artifact serialization
├── interface.py          # Interactive Streamlit UI with file upload & tabs
├── README.md             # This technical document
├── data/
│   └── .gitkeep          # Training data folder
├── artifacts/
│   ├── .gitkeep          # Checkpoints folder
│   └── tfidf_vectorizer.joblib  # Serialized vectorizer
└── tests/
    └── test_resume_job_matching.py  # Comprehensive unit test suite (12 tests)
```

---

## 6. Testing & Running

### Run Unit Tests
```bash
python -m pytest modules/resume_job_matching/tests/ -v
```

### Run Platform Integration Check
```bash
python -m pytest -v
```

### Launch the Application
```bash
streamlit run app.py
```
*(Select **Resume–Job Matching** from the sidebar)*.
