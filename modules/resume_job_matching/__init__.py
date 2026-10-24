"""
TalentBridge AI - Resume–Job Matching Module
Member 1: Production-grade hybrid matching, document parsing, and ATS optimization.
"""

from .interface import render
from .model import ResumeJobMatcher
from .preprocessing import (
    audit_resume_structure,
    clean_text,
    extract_keywords,
    extract_taxonomy_skills,
    find_skill_gap_detailed,
    parse_document,
)

__all__ = [
    "ResumeJobMatcher",
    "clean_text",
    "extract_keywords",
    "extract_taxonomy_skills",
    "find_skill_gap_detailed",
    "audit_resume_structure",
    "parse_document",
    "render",
]
