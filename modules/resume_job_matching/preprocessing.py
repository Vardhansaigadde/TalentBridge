"""
Text preprocessing and keyword extraction utilities for Resume–Job Matching.
"""

import re
from typing import Dict, List, Set
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

from .config import ADDITIONAL_STOPWORDS


def clean_text(text: str) -> str:
    """
    Cleans raw text by:
    - Lowercasing
    - Removing URLs and email addresses
    - Normalizing whitespace and punctuation
    - Keeping alphanumeric characters and relevant tech symbols (+, #)
    """
    if not text or not isinstance(text, str):
        return ""

    # Lowercase
    cleaned = text.lower()

    # Remove URLs
    cleaned = re.sub(r"https?://\S+|www\.\S+", " ", cleaned)

    # Remove email addresses
    cleaned = re.sub(r"\S+@\S+", " ", cleaned)

    # Replace special separators/bullets with space
    cleaned = re.sub(r"[\r\n\t•·|/\\_()\[\]{}:;\"*~`]", " ", cleaned)

    # Keep letters, numbers, hyphens, and specific programming terms (c++, c#)
    cleaned = re.sub(r"[^a-z0-9+#\-\s]", " ", cleaned)

    # Collapse multiple spaces
    cleaned = re.sub(r"\s+", " ", cleaned).strip()

    return cleaned


def extract_keywords(text: str, top_n: int = 35) -> List[str]:
    """
    Extracts informative keywords (unigrams and technical bigrams) from cleaned text,
    filtering out standard English stop words and common job-posting filler phrases.
    """
    cleaned = clean_text(text)
    if not cleaned:
        return []

    tokens = cleaned.split()
    all_stopwords: Set[str] = set(ENGLISH_STOP_WORDS).union(ADDITIONAL_STOPWORDS)

    # Filter tokens by length and stopword membership
    meaningful_tokens: List[str] = [
        tok for tok in tokens
        if len(tok) >= 3 and tok not in all_stopwords and not tok.isdigit()
    ]

    # Frequency counting
    freq_map: Dict[str, int] = {}
    for tok in meaningful_tokens:
        freq_map[tok] = freq_map.get(tok, 0) + 1

    # Sort by frequency descending
    sorted_keywords = sorted(freq_map.keys(), key=lambda k: freq_map[k], reverse=True)
    return sorted_keywords[:top_n]


def find_skill_gap(resume_text: str, job_text: str, top_n_keywords: int = 30) -> Dict[str, List[str]]:
    """
    Compares the significant terms in the job description against the resume text
    to identify matched skills and potential missing keywords / skill gaps.
    """
    job_keywords = extract_keywords(job_text, top_n=top_n_keywords)
    cleaned_resume = clean_text(resume_text)
    resume_tokens = set(cleaned_resume.split())

    matched: List[str] = []
    missing: List[str] = []

    for kw in job_keywords:
        # Check if single token or phrase is in resume
        if kw in resume_tokens or kw in cleaned_resume:
            matched.append(kw)
        else:
            missing.append(kw)

    return {
        "job_keywords": job_keywords,
        "matched_keywords": matched,
        "missing_keywords": missing,
    }
