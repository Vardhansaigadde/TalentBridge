"""
Unit tests for the Resume–Job Matching module.
Tests preprocessing, keyword extraction, TF-IDF cosine similarity, and gap analysis.
"""

import pytest

from modules.resume_job_matching.config import SAMPLE_JOB_DESCRIPTION, SAMPLE_RESUME
from modules.resume_job_matching.model import ResumeJobMatcher
from modules.resume_job_matching.preprocessing import (
    clean_text,
    extract_keywords,
    find_skill_gap,
)


def test_clean_text_basic():
    raw = "Senior Software Developer with 5+ years experience! Visit https://example.com or email me@work.com"
    cleaned = clean_text(raw)
    assert "https" not in cleaned
    assert "me@work.com" not in cleaned
    assert "senior software developer" in cleaned
    assert "!" not in cleaned


def test_clean_text_empty_and_none():
    assert clean_text("") == ""
    assert clean_text(None) == ""


def test_extract_keywords():
    text = "Python Docker Kubernetes AWS Python Fastapi Microservices Python"
    keywords = extract_keywords(text, top_n=5)
    assert "python" in keywords
    # Python is most frequent
    assert keywords[0] == "python"
    assert len(keywords) <= 5


def test_find_skill_gap():
    job = "Requires Python, Kubernetes, Kafka, and Docker."
    resume = "Jane Doe has extensive experience in Python, Docker, and PostgreSQL."
    result = find_skill_gap(resume, job)

    assert "python" in result["matched_keywords"]
    assert "docker" in result["matched_keywords"]
    assert "kubernetes" in result["missing_keywords"]
    assert "kafka" in result["missing_keywords"]


def test_similarity_identical_texts():
    matcher = ResumeJobMatcher()
    sample = "Senior Python engineer with AWS, Docker, and FastAPI experience."
    score = matcher.compute_similarity(sample, sample)
    assert score >= 0.99


def test_similarity_disjoint_texts():
    matcher = ResumeJobMatcher()
    t1 = "Pediatric surgeon hospital clinical healthcare patient biology"
    t2 = "Kubernetes Docker terraform microservices backend python devops"
    score = matcher.compute_similarity(t1, t2)
    # Expected to be very low
    assert score < 0.20


def test_similarity_empty_inputs():
    matcher = ResumeJobMatcher()
    assert matcher.compute_similarity("", "Python engineer") == 0.0
    assert matcher.compute_similarity("Developer", "") == 0.0
    assert matcher.compute_similarity("", "") == 0.0


def test_predict_structure():
    matcher = ResumeJobMatcher()
    results = matcher.predict(SAMPLE_RESUME, SAMPLE_JOB_DESCRIPTION)

    required_keys = [
        "similarity_score",
        "match_percentage",
        "match_level",
        "match_color",
        "verdict",
        "matched_keywords",
        "missing_keywords",
        "top_job_keywords",
        "resume_word_count",
        "job_word_count",
    ]
    for key in required_keys:
        assert key in results

    assert 0.0 <= results["similarity_score"] <= 1.0
    assert 0.0 <= results["match_percentage"] <= 100.0
    assert results["match_level"] in ["High Match", "Moderate Match", "Low Match"]
    assert len(results["matched_keywords"]) > 0
