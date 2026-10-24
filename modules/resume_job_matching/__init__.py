"""
TalentBridge AI - Resume–Job Matching Module
Member 1: Core baseline implementation for text similarity matching.
"""

from .model import ResumeJobMatcher
from .preprocessing import clean_text, extract_keywords
from .interface import render

__all__ = ["ResumeJobMatcher", "clean_text", "extract_keywords", "render"]
