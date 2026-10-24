"""
Resume–Job Matching Machine Learning Model.
Implements TF-IDF feature extraction, Cosine Similarity matching, and gap analytics.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Tuple
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .config import (
    MODEL_PATH,
    SUBLINEAR_TF,
    TFIDF_MAX_FEATURES,
    TFIDF_NGRAM_RANGE,
    THRESHOLD_HIGH,
    THRESHOLD_MODERATE,
)
from .preprocessing import clean_text, find_skill_gap


class ResumeJobMatcher:
    """
    Computes semantic text similarity and keyword alignment
    between candidate resumes and job descriptions using TF-IDF and Cosine Similarity.
    """

    def __init__(self, vectorizer: Optional[TfidfVectorizer] = None) -> None:
        self.vectorizer = vectorizer or TfidfVectorizer(
            ngram_range=TFIDF_NGRAM_RANGE,
            max_features=TFIDF_MAX_FEATURES,
            sublinear_tf=SUBLINEAR_TF,
            stop_words="english",
        )
        self.is_fitted = False

    def fit(self, corpus: list[str]) -> "ResumeJobMatcher":
        """Fits the internal TF-IDF vectorizer on a text corpus."""
        cleaned_corpus = [clean_text(doc) for doc in corpus if doc]
        if cleaned_corpus:
            self.vectorizer.fit(cleaned_corpus)
            self.is_fitted = True
        return self

    def save(self, filepath: Optional[Path] = None) -> Path:
        """Serializes the fitted vectorizer to disk."""
        target_path = Path(filepath or MODEL_PATH)
        target_path.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(self.vectorizer, target_path)
        return target_path

    @classmethod
    def load(cls, filepath: Optional[Path] = None) -> "ResumeJobMatcher":
        """Loads a pre-fitted vectorizer from disk if available."""
        target_path = Path(filepath or MODEL_PATH)
        if target_path.exists():
            vec = joblib.load(target_path)
            instance = cls(vectorizer=vec)
            instance.is_fitted = True
            return instance
        return cls()

    def compute_similarity(self, resume_text: str, job_text: str) -> float:
        """
        Computes the cosine similarity score between resume and job description.
        Returns a float between 0.0 and 1.0.
        """
        cleaned_resume = clean_text(resume_text)
        cleaned_job = clean_text(job_text)

        if not cleaned_resume or not cleaned_job:
            return 0.0

        # If vectorizer is not pre-fitted on a global corpus, fit on the document pair
        if not self.is_fitted:
            local_vec = TfidfVectorizer(
                ngram_range=TFIDF_NGRAM_RANGE,
                sublinear_tf=SUBLINEAR_TF,
                stop_words="english",
            )
            tfidf_matrix = local_vec.fit_transform([cleaned_resume, cleaned_job])
            sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        else:
            vectors = self.vectorizer.transform([cleaned_resume, cleaned_job])
            sim = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

        # Bound score between 0.0 and 1.0
        return float(np.clip(sim, 0.0, 1.0))

    def predict(self, resume_text: str, job_text: str) -> Dict[str, Any]:
        """
        Performs full end-to-end matching analysis:
        - Cosine similarity calculation
        - Threshold classification (High, Moderate, Low)
        - Keyword overlap and skill gap analysis
        """
        score = self.compute_similarity(resume_text, job_text)
        percentage = round(score * 100.0, 2)

        if percentage >= THRESHOLD_HIGH:
            level = "High Match"
            level_color = "#22c55e"
            verdict = "Strong textual alignment with the key responsibilities and technologies in the job posting."
        elif percentage >= THRESHOLD_MODERATE:
            level = "Moderate Match"
            level_color = "#f59e0b"
            verdict = "Moderate overlap. Candidate has foundational skills but could address notable skill gaps."
        else:
            level = "Low Match"
            level_color = "#ef4444"
            verdict = "Low textual overlap. Significant vocabulary and technology discrepancies detected."

        gap_analysis = find_skill_gap(resume_text, job_text)

        resume_word_count = len(clean_text(resume_text).split())
        job_word_count = len(clean_text(job_text).split())

        return {
            "similarity_score": score,
            "match_percentage": percentage,
            "match_level": level,
            "match_color": level_color,
            "verdict": verdict,
            "matched_keywords": gap_analysis["matched_keywords"],
            "missing_keywords": gap_analysis["missing_keywords"],
            "top_job_keywords": gap_analysis["job_keywords"],
            "resume_word_count": resume_word_count,
            "job_word_count": job_word_count,
        }
