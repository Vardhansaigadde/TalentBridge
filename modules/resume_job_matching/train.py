"""
Training and artifact serialization script for Resume–Job Matching.
Fits a domain-level TF-IDF vectorizer on seed technical job descriptions and resumes.
"""

import sys
from pathlib import Path

# Add project root to path if executed standalone
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from modules.resume_job_matching.config import (
    ARTIFACTS_DIR,
    MODEL_PATH,
    SAMPLE_JOB_DESCRIPTION,
    SAMPLE_RESUME,
)
from modules.resume_job_matching.model import ResumeJobMatcher

# Seed corpus representing common technical job postings and developer resumes
SEED_CORPUS = [
    SAMPLE_RESUME,
    SAMPLE_JOB_DESCRIPTION,
    """Frontend React Engineer: Experience in React, TypeScript, Redux, CSS, HTML5,
    Next.js, Tailwind CSS, Jest, GraphQL, REST APIs, Webpack, Responsive Design.""",
    """Data Scientist / ML Engineer: Python, NumPy, Pandas, Scikit-learn, PyTorch,
    TensorFlow, NLP, Computer Vision, Docker, SQL, Statistics, Data Modeling, Feature Engineering.""",
    """DevOps and Site Reliability Engineer: Kubernetes, Docker, Terraform, AWS, GCP,
    CI/CD pipelines, Prometheus, Grafana, Linux, Bash, Ansible, Networking, Security.""",
    """Product Manager / Business Analyst: Agile, Scrum, JIRA, User Stories, Roadmaps,
    Market Analysis, Cross-functional Leadership, KPI tracking, Product Strategy.""",
]


def train_and_save_vectorizer(output_path: Path = MODEL_PATH) -> Path:
    """
    Fits the ResumeJobMatcher vectorizer on the seed corpus and saves the artifact.
    """
    print(f"[Training] Initializing TF-IDF Vectorizer with {len(SEED_CORPUS)} seed documents...")
    matcher = ResumeJobMatcher()
    matcher.fit(SEED_CORPUS)

    saved_path = matcher.save(output_path)
    print(f"[Artifact Saved] Model successfully serialized to: {saved_path}")
    return saved_path


if __name__ == "__main__":
    train_and_save_vectorizer()
