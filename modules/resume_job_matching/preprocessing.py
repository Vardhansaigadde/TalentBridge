"""
Text preprocessing, document parsing (PDF/DOCX/TXT), skills taxonomy extraction,
and ATS structural diagnostics for Resume–Job Matching.
"""

import io
import re
from typing import Any, BinaryIO, Dict, List, Set, Union
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

from .config import (
    ADDITIONAL_STOPWORDS,
    ESSENTIAL_RESUME_SECTIONS,
    SKILLS_TAXONOMY,
    STRONG_ACTION_VERBS,
)


def parse_document(file_data: Union[BinaryIO, bytes], filename: str) -> str:
    """
    Extracts plain text from uploaded files supporting .pdf, .docx, and .txt.
    """
    if not file_data or not filename:
        return ""

    ext = filename.lower().split(".")[-1]
    raw_bytes = file_data.read() if hasattr(file_data, "read") else file_data

    # Reset stream pointer if it was a file object
    if hasattr(file_data, "seek"):
        file_data.seek(0)

    try:
        if ext == "pdf":
            import fitz  # PyMuPDF
            doc = fitz.open(stream=raw_bytes, filetype="pdf")
            text_pages = [page.get_text() for page in doc]
            return "\n".join(text_pages).strip()

        elif ext in ("docx", "doc"):
            import docx
            doc = docx.Document(io.BytesIO(raw_bytes))
            paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
            for table in doc.tables:
                for row in table.rows:
                    for cell in row.cells:
                        if cell.text.strip():
                            paragraphs.append(cell.text.strip())
            return "\n".join(paragraphs).strip()

        elif ext in ("txt", "md"):
            try:
                return raw_bytes.decode("utf-8")
            except UnicodeDecodeError:
                return raw_bytes.decode("latin-1", errors="ignore")

        else:
            raise ValueError(f"Unsupported file format: '.{ext}'. Supported formats are: PDF, DOCX, TXT.")

    except Exception as exc:
        raise RuntimeError(f"Error parsing document '{filename}': {str(exc)}") from exc


def clean_text(text: str) -> str:
    """
    Cleans raw text for NLP processing:
    - Lowercase
    - Removes URLs and email addresses
    - Normalizes punctuation, bullet points, and redundant whitespace
    - Preserves technology terms with +, #, and hyphens (e.g. c++, c#, ci/cd)
    """
    if not text or not isinstance(text, str):
        return ""

    cleaned = text.lower()
    cleaned = re.sub(r"https?://\S+|www\.\S+", " ", cleaned)
    cleaned = re.sub(r"\S+@\S+", " ", cleaned)
    cleaned = re.sub(r"[\r\n\t•·|/\\_()\[\]{}:;\"*~`]", " ", cleaned)
    cleaned = re.sub(r"[^a-z0-9+#\-\s]", " ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def extract_taxonomy_skills(text: str) -> Dict[str, List[str]]:
    """
    Scans input text against the curated technical skills taxonomy.
    Matches both single-token and multi-word phrases (e.g., 'rest api', 'spring boot').
    Returns skills grouped by domain category.
    """
    cleaned = clean_text(text)
    if not cleaned:
        return {cat: [] for cat in SKILLS_TAXONOMY}

    detected_by_category: Dict[str, List[str]] = {}

    for category, skill_set in SKILLS_TAXONOMY.items():
        found_in_category: List[str] = []
        for skill in skill_set:
            # Word boundary matching to avoid partial token false positives (e.g., 'go' inside 'good')
            escaped_skill = re.escape(skill)
            pattern = rf"(?:\b|\s|^){escaped_skill}(?:\b|\s|$)"
            if re.search(pattern, cleaned):
                found_in_category.append(skill)
        detected_by_category[category] = sorted(found_in_category)

    return detected_by_category


def extract_flat_skills(text: str) -> Set[str]:
    """
    Extracts all taxonomy skills found in text as a flat set of strings.
    """
    categorized = extract_taxonomy_skills(text)
    all_skills: Set[str] = set()
    for skills in categorized.values():
        all_skills.update(skills)
    return all_skills


def find_skill_gap_detailed(resume_text: str, job_text: str) -> Dict[str, Any]:
    """
    Performs comprehensive skill gap analysis between resume and job description.
    Returns categorized matches, missing items, and coverage ratios.
    """
    resume_categorized = extract_taxonomy_skills(resume_text)
    job_categorized = extract_taxonomy_skills(job_text)

    resume_all = extract_flat_skills(resume_text)
    job_all = extract_flat_skills(job_text)

    matched_skills = sorted(list(job_all.intersection(resume_all)))
    missing_skills = sorted(list(job_all.difference(resume_all)))
    bonus_skills = sorted(list(resume_all.difference(job_all)))

    category_breakdown: Dict[str, Dict[str, Any]] = {}
    for cat in SKILLS_TAXONOMY.keys():
        j_skills = set(job_categorized.get(cat, []))
        r_skills = set(resume_categorized.get(cat, []))
        c_matched = sorted(list(j_skills.intersection(r_skills)))
        c_missing = sorted(list(j_skills.difference(r_skills)))
        coverage = round((len(c_matched) / len(j_skills) * 100), 1) if j_skills else 100.0

        category_breakdown[cat] = {
            "required_count": len(j_skills),
            "matched_count": len(c_matched),
            "coverage_percent": coverage,
            "matched": c_matched,
            "missing": c_missing,
        }

    skills_match_ratio = (len(matched_skills) / len(job_all)) if job_all else 1.0

    return {
        "job_skills": sorted(list(job_all)),
        "resume_skills": sorted(list(resume_all)),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "bonus_skills": bonus_skills,
        "category_breakdown": category_breakdown,
        "skills_match_ratio": skills_match_ratio,
        "skills_match_percentage": round(skills_match_ratio * 100.0, 1),
    }


def audit_resume_structure(resume_text: str) -> Dict[str, Any]:
    """
    Performs ATS format diagnostics:
    - Length & word count assessment
    - Essential section presence checks
    - Action verbs density
    - Quantification & metrics check
    - Actionable recommendations list
    """
    if not resume_text:
        return {
            "word_count": 0,
            "length_status": "Empty",
            "sections_present": [],
            "sections_missing": list(ESSENTIAL_RESUME_SECTIONS.keys()),
            "action_verbs_found": [],
            "action_verb_count": 0,
            "quantification_count": 0,
            "recommendations": ["Please upload or paste your resume to receive an ATS audit."],
        }

    cleaned = clean_text(resume_text)
    words = cleaned.split()
    word_count = len(words)

    # Word count evaluation
    if word_count < 250:
        length_status = "Too Short (< 250 words)"
        length_color = "#ef4444"
    elif word_count <= 850:
        length_status = "Optimal (250 - 850 words)"
        length_color = "#22c55e"
    else:
        length_status = "Long (> 850 words)"
        length_color = "#f59e0b"

    # Section Detection
    lower_raw = resume_text.lower()
    sections_present: List[str] = []
    sections_missing: List[str] = []

    for section_name, keywords in ESSENTIAL_RESUME_SECTIONS.items():
        found = any(re.search(rf"\b{re.escape(kw)}\b", lower_raw) for kw in keywords)
        if found:
            sections_present.append(section_name)
        else:
            sections_missing.append(section_name)

    # Action Verbs Count
    action_verbs_found = sorted(list(STRONG_ACTION_VERBS.intersection(set(words))))

    # Quantification detection (e.g. 50%, $10k, 10x, 5 years, 30+)
    metrics_patterns = re.findall(r"\b\d+[%+xXkKmM]?\b|\$\d+", resume_text)
    quantification_count = len(metrics_patterns)

    # Actionable Recommendations
    recommendations: List[str] = []
    if word_count < 250:
        recommendations.append("Expand on your project deliverables and technical responsibilities to reach at least 300 words.")
    if "Professional Experience" in sections_missing:
        recommendations.append("Ensure your work history is clearly marked under an 'Experience' or 'Work History' header.")
    if "Education" in sections_missing:
        recommendations.append("Add an explicit 'Education' or 'Academic Background' section.")
    if len(action_verbs_found) < 5:
        recommendations.append(
            f"Use more impactful action verbs (found {len(action_verbs_found)}). Begin bullets with verbs like 'Architected', 'Engineered', 'Optimized', or 'Automated'."
        )
    if quantification_count < 3:
        recommendations.append("Quantify your impact with measurable metrics (e.g., 'reduced latency by 40%', 'managed $50k budget', 'led 6 engineers').")

    if not recommendations:
        recommendations.append("Resume demonstrates strong ATS structure, clear headers, high action-verb density, and quantifiable impact!")

    return {
        "word_count": word_count,
        "length_status": length_status,
        "length_color": length_color,
        "sections_present": sections_present,
        "sections_missing": sections_missing,
        "action_verbs_found": action_verbs_found,
        "action_verb_count": len(action_verbs_found),
        "quantification_count": quantification_count,
        "recommendations": recommendations,
    }


# Backwards compatibility helper for baseline interface
def extract_keywords(text: str, top_n: int = 35) -> List[str]:
    """Extracts general vocabulary keywords."""
    cleaned = clean_text(text)
    if not cleaned:
        return []
    tokens = cleaned.split()
    all_stopwords = set(ENGLISH_STOP_WORDS).union(ADDITIONAL_STOPWORDS)
    filtered = [t for t in tokens if len(t) >= 3 and t not in all_stopwords and not t.isdigit()]
    freq: Dict[str, int] = {}
    for t in filtered:
        freq[t] = freq.get(t, 0) + 1
    return sorted(freq.keys(), key=lambda k: freq[k], reverse=True)[:top_n]


def find_skill_gap(resume_text: str, job_text: str, top_n_keywords: int = 30) -> Dict[str, List[str]]:
    """Legacy helper maintained for backward compatibility."""
    detailed = find_skill_gap_detailed(resume_text, job_text)
    return {
        "job_keywords": detailed["job_skills"][:top_n_keywords],
        "matched_keywords": detailed["matched_skills"],
        "missing_keywords": detailed["missing_skills"],
    }
