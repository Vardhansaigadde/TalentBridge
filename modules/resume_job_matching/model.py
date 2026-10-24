"""
Resume–Job Matching Hybrid Machine Learning Model.
Combines TF-IDF vectorization with Domain Skills Taxonomy and ATS Diagnostics.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional
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
    WEIGHT_SKILLS_OVERLAP,
    WEIGHT_TEXTUAL_SIMILARITY,
)
from .preprocessing import (
    audit_resume_structure,
    clean_text,
    find_skill_gap_detailed,
)


class ResumeJobMatcher:
    """
    Hybrid Resume–Job Matching engine:
    1. Lexical & Contextual similarity via TF-IDF + Cosine Distance
    2. Explicit Domain Competencies & Skills Taxonomy matching
    3. ATS formatting, impact verbs, and structural audit
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
        """Fits the TF-IDF vectorizer on a corpus."""
        cleaned = [clean_text(doc) for doc in corpus if doc]
        if cleaned:
            self.vectorizer.fit(cleaned)
            self.is_fitted = True
        return self

    def save(self, filepath: Optional[Path] = None) -> Path:
        """Serializes the fitted vectorizer."""
        target = Path(filepath or MODEL_PATH)
        target.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(self.vectorizer, target)
        return target

    @classmethod
    def load(cls, filepath: Optional[Path] = None) -> "ResumeJobMatcher":
        """Loads a pre-fitted vectorizer from disk if present."""
        target = Path(filepath or MODEL_PATH)
        if target.exists():
            vec = joblib.load(target)
            instance = cls(vectorizer=vec)
            instance.is_fitted = True
            return instance
        return cls()

    def compute_similarity(self, resume_text: str, job_text: str) -> float:
        """
        Computes cosine similarity of TF-IDF vectors.
        """
        cleaned_resume = clean_text(resume_text)
        cleaned_job = clean_text(job_text)

        if not cleaned_resume or not cleaned_job:
            return 0.0

        if not self.is_fitted:
            local_vec = TfidfVectorizer(
                ngram_range=TFIDF_NGRAM_RANGE,
                sublinear_tf=SUBLINEAR_TF,
                stop_words="english",
            )
            matrix = local_vec.fit_transform([cleaned_resume, cleaned_job])
            sim = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
        else:
            vectors = self.vectorizer.transform([cleaned_resume, cleaned_job])
            sim = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

        return float(np.clip(sim, 0.0, 1.0))

    def predict(self, resume_text: str, job_text: str) -> Dict[str, Any]:
        """
        Executes complete hybrid analysis:
        - TF-IDF textual similarity
        - Domain skills taxonomy overlap
        - Weighted composite score
        - ATS structural audit
        - Actionable step-by-step optimization recommendations
        """
        # 1. Textual Similarity
        text_sim = self.compute_similarity(resume_text, job_text)
        text_pct = round(text_sim * 100.0, 1)

        # 2. Detailed Skills Taxonomy Analysis
        skill_analysis = find_skill_gap_detailed(resume_text, job_text)
        skills_ratio = skill_analysis["skills_match_ratio"]
        skills_pct = skill_analysis["skills_match_percentage"]

        # 3. Composite Weighted Score
        if skill_analysis["job_skills"]:
            composite_score = (WEIGHT_SKILLS_OVERLAP * skills_ratio) + (WEIGHT_TEXTUAL_SIMILARITY * text_sim)
        else:
            # Fallback to pure TF-IDF if job description had no detected taxonomy skills
            composite_score = text_sim

        composite_pct = round(composite_score * 100.0, 1)

        # 4. Classification Tier
        if composite_pct >= THRESHOLD_HIGH:
            level = "High Match"
            level_color = "#22c55e"
            verdict = "Strong candidate alignment! High technical skill coverage and comprehensive experience correspondence."
        elif composite_pct >= THRESHOLD_MODERATE:
            level = "Moderate Match"
            level_color = "#f59e0b"
            verdict = "Solid foundation with moderate overlap. Addressing the identified skill gaps will notably improve suitability."
        else:
            level = "Low Match"
            level_color = "#ef4444"
            verdict = "Limited overlap detected. Crucial job requirements and core technologies are missing from the resume."

        # 5. ATS Structural Audit
        ats_audit = audit_resume_structure(resume_text)

        # 6. Actionable Optimization Strategy
        optimization_plan: List[str] = []
        if skill_analysis["missing_skills"]:
            top_missing = ", ".join(f"'{s}'" for s in skill_analysis["missing_skills"][:5])
            optimization_plan.append(
                f"**Skill Gap Priority:** Add evidence of experience with high-demand job skills: {top_missing}."
            )
        if ats_audit["sections_missing"]:
            missing_sec = ", ".join(ats_audit["sections_missing"])
            optimization_plan.append(f"**ATS Section Warning:** Add missing standard sections: {missing_sec}.")
        if ats_audit["action_verb_count"] < 6:
            optimization_plan.append(
                "**Action Verb Impact:** Strengthen bullet points with action verbs (e.g., 'Architected', 'Engineered', 'Optimized')."
            )
        if ats_audit["quantification_count"] < 3:
            optimization_plan.append(
                "**Quantify Results:** Add numerical metrics, scale indicators (e.g. 'reduced latency by 40%', 'processed 5M requests')."
            )
        if not optimization_plan:
            optimization_plan.append("Your resume is well-tailored for this role with strong skill coverage and high ATS readiness.")

        # Provide both backward-compatible keys and rich new keys
        return {
            "similarity_score": composite_score,
            "match_percentage": composite_pct,
            "match_level": level,
            "match_color": level_color,
            "verdict": verdict,
            "textual_similarity_percentage": text_pct,
            "skills_overlap_percentage": skills_pct,
            "matched_keywords": skill_analysis["matched_skills"],
            "missing_keywords": skill_analysis["missing_skills"],
            "bonus_skills": skill_analysis["bonus_skills"],
            "top_job_keywords": skill_analysis["job_skills"],
            "category_breakdown": skill_analysis["category_breakdown"],
            "ats_audit": ats_audit,
            "optimization_plan": optimization_plan,
            "resume_word_count": ats_audit["word_count"],
            "job_word_count": len(clean_text(job_text).split()),
        }
