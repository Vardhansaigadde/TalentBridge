# Module 1: Resume–Job Matching Engine

**Assigned Lead:** Member 1  
**Status:** ✅ Active Baseline Implemented  
**Package:** `modules.resume_job_matching`

---

## 1. Overview & Objective

The **Resume–Job Matching** module is designed to provide immediate, transparent feedback to candidates and recruiters by assessing textual alignment between a candidate's resume and a target job description. It extracts high-signal domain vocabulary, computes vector-space distance, and highlights actionable skill gaps.

---

## 2. Machine Learning Architecture

### Algorithm Formulation
This baseline implementation utilizes a dual **Term Frequency-Inverse Document Frequency (TF-IDF)** vectorization model combined with **Cosine Distance** measurement:

1. **Text Preprocessing (`preprocessing.py`):**
   - Normalization: Case folding, URL removal, email stripping, punctuation filtering.
   - Stopword Elimination: Merges English stop words with recruiting noise phrases (e.g., *requirements, responsibilities, years*).
   - Domain N-Grams: Unigrams and bigrams are extracted to capture compound technologies (e.g., `rest api`, `ci cd`).

2. **Vector Space Model (`model.py`):**
   - Sublinear term frequency scaling: $tf = 1 + \log(tf)$ for positive frequencies.
   - Vector projection: Text inputs $D_{resume}$ and $D_{job}$ are projected into an $N$-dimensional sparse vector space.

3. **Cosine Similarity:**
   $$\text{Similarity}(u, v) = \frac{u \cdot v}{\|u\|_2 \|v\|_2}$$
   - Produces a normalized scalar score in the interval $[0.0, 1.0]$.
   - Mapped to a percentage: $\text{Score} = \text{Similarity} \times 100\%$.

4. **Skill Gap & Keyword Overlap Analysis:**
   - Evaluates token intersection between salient Job Description terms and the Resume text.
   - Outputs:
     - `matched_keywords`: Terms present in both texts.
     - `missing_keywords`: High-value job requirements absent from the resume.

---

## 3. Inputs & Outputs Contract

### Expected Inputs
- **Candidate Resume:** Plain text string containing candidate experience, skills, and education.
- **Job Description:** Plain text string containing the job requirements and responsibilities.

### Expected Outputs
- `similarity_score`: Float between `0.0` and `1.0`.
- `match_percentage`: Float between `0.0%` and `100.0%`.
- `match_level`: Categorical tier (`High Match` $\ge 70\%$, `Moderate Match` $40\%-69\%$, `Low Match` $<40\%$).
- `matched_keywords`: List of identified overlapping competencies.
- `missing_keywords`: List of identified candidate gaps.
- `verdict`: Human-readable narrative explanation.

---

## 4. Ethical AI & Practical Limitations

> ⚠️ **CRITICAL DISCLAIMER: Text-similarity is NOT hiring probability.**
> A high similarity score demonstrates keyword and contextual correspondence. It does **not** signify a guarantee of an interview, admission, or job offer. Real-world hiring requires holistic human review evaluating soft skills, creative problem solving, cultural contribution, and practical code execution.

### Known Limitations of Current Baseline:
- **Synonym Invariance:** TF-IDF treats distinct lexical tokens separately (e.g., `GCP` vs `Google Cloud Platform` unless n-grams capture it).
- **Context Blindness:** Negations (e.g., *"not experienced in Java"*) may still register as term frequency.
- **Formatting Dependence:** Requires clean plain text; PDF parsing will be handled by upstream document loaders.

---

## 5. File Structure

```
modules/resume_job_matching/
├── __init__.py           # Package exports
├── config.py             # Parameters, sample profiles, and thresholds
├── preprocessing.py      # Cleaning and skill gap extraction
├── model.py              # ResumeJobMatcher class and inference pipeline
├── train.py              # Offline vectorizer training & serialization script
├── interface.py          # Streamlit UI render() implementation
├── README.md             # Module documentation
├── data/
│   └── .gitkeep          # Training datasets directory
├── artifacts/
│   └── .gitkeep          # Serialized vectorizer (.joblib)
└── tests/
    └── test_resume_job_matching.py  # Pytest suite
```

---

## 6. Testing & Execution

### Run Unit Tests
From the project root:
```bash
pytest modules/resume_job_matching/tests/ -v
```

### Run Model Training & Serialization
```bash
python modules/resume_job_matching/train.py
```

### Launch Interactive Interface
```bash
streamlit run app.py
```
Navigate to **1. Resume–Job Matching** in the left sidebar.
