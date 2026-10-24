"""
Configuration settings, skills taxonomies, presets, and constants for Resume–Job Matching.
"""

from pathlib import Path
from typing import Dict, List, Set

# Paths
MODULE_DIR = Path(__file__).resolve().parent
DATA_DIR = MODULE_DIR / "data"
ARTIFACTS_DIR = MODULE_DIR / "artifacts"
MODEL_PATH = ARTIFACTS_DIR / "tfidf_vectorizer.joblib"

# Model Hyperparameters
TFIDF_MAX_FEATURES = 6000
TFIDF_NGRAM_RANGE = (1, 2)
SUBLINEAR_TF = True

# Composite Scoring Weights
WEIGHT_SKILLS_OVERLAP = 0.55
WEIGHT_TEXTUAL_SIMILARITY = 0.45

# Score Categorization Thresholds (in percentage)
THRESHOLD_HIGH = 75.0
THRESHOLD_MODERATE = 45.0

# Curated Technical Domain Taxonomy (Categorized Skills & Tools)
SKILLS_TAXONOMY: Dict[str, Set[str]] = {
    "Programming Languages": {
        "python", "java", "c++", "c#", "javascript", "typescript", "golang", "go",
        "rust", "ruby", "php", "swift", "kotlin", "scala", "r", "sql", "bash", "shell",
        "html", "css", "c"
    },
    "Frameworks & Libraries": {
        "fastapi", "django", "flask", "react", "react.js", "next.js", "node.js", "express",
        "angular", "vue", "vue.js", "spring boot", "spring", "asp.net", ".net", "graphql",
        "rest api", "restful api", "tailwind", "redux", "jquery", "bootstrap"
    },
    "Cloud & DevOps": {
        "aws", "azure", "gcp", "google cloud", "docker", "kubernetes", "k8s", "terraform",
        "ci/cd", "ci cd", "github actions", "gitlab ci", "jenkins", "ansible", "helm",
        "linux", "nginx", "prometheus", "grafana", "cloudformation"
    },
    "Databases & Storage": {
        "postgresql", "postgres", "mysql", "mongodb", "redis", "cassandra", "elasticsearch",
        "dynamodb", "sqlite", "oracle", "mariadb", "snowflake", "bigquery"
    },
    "Data & AI/ML": {
        "pytorch", "tensorflow", "scikit-learn", "sklearn", "pandas", "numpy", "scipy",
        "nlp", "natural language processing", "llm", "llms", "computer vision", "opencv",
        "spark", "apache spark", "airflow", "tableau", "power bi", "deep learning", "machine learning"
    },
    "Architecture & Methodologies": {
        "microservices", "system design", "distributed systems", "agile", "scrum", "jira",
        "unit testing", "pytest", "test driven development", "tdd", "git", "oop",
        "object oriented programming", "event driven architecture", "kafka", "rabbitmq"
    },
}

# Strong Action Verbs for ATS Impact Scoring
STRONG_ACTION_VERBS: Set[str] = {
    "architected", "engineered", "developed", "designed", "implemented", "scaled",
    "optimized", "accelerated", "reduced", "automated", "spearheaded", "orchestrated",
    "deployed", "refactored", "integrated", "streamlined", "built", "launched",
    "mentored", "collaborated", "managed", "delivered", "increased", "decreased"
}

# Standard Resume Section Headers
ESSENTIAL_RESUME_SECTIONS: Dict[str, List[str]] = {
    "Contact Info": ["email", "phone", "linkedin", "github"],
    "Professional Experience": ["experience", "employment", "work history", "professional background"],
    "Education": ["education", "academic", "degree", "university", "bachelor", "master", "phd"],
    "Skills": ["skills", "technical skills", "technologies", "competencies", "tools"],
    "Projects": ["projects", "personal projects", "portfolio", "key initiatives"],
}

# Stopwords & Recruiting Noise Words
ADDITIONAL_STOPWORDS: Set[str] = {
    "responsibilities", "requirements", "experience", "years", "candidate", "role",
    "team", "work", "working", "looking", "plus", "skills", "ability", "strong",
    "good", "excellent", "knowledge", "required", "preferred", "must", "have",
    "including", "opportunity", "company", "position", "demonstrated", "familiarity"
}

# Sample Resumes
SAMPLE_RESUME = """Jane Doe
Senior Python Backend Developer | Distributed Systems & Cloud
Email: jane.doe@example.com | GitHub: github.com/janedoe | LinkedIn: linkedin.com/in/janedoe

PROFESSIONAL SUMMARY
Results-driven software engineer with 5+ years of experience building high-throughput microservices, REST APIs, and data pipelines using Python, FastAPI, and Docker. Proven track record of improving database query performance by 40% and deploying scalable containerized applications on AWS.

CORE TECHNICAL SKILLS
- Languages: Python, SQL, Bash, JavaScript
- Frameworks & Libraries: FastAPI, Flask, Django, Pydantic, SQLAlchemy, Pandas, Scikit-learn
- Databases: PostgreSQL, MySQL, Redis
- Cloud & DevOps: AWS, Docker, CI/CD, GitHub Actions, Git, Linux
- Architecture: REST APIs, Microservices, Event-Driven Architecture, Unit Testing (pytest)

WORK EXPERIENCE
Senior Backend Engineer | CloudScale Tech (2022 - Present)
- Architected and deployed 12+ asynchronous microservices using FastAPI and Docker, handling 5M+ daily requests.
- Implemented Redis caching layer reducing database read load by 60% and decreasing p99 latency from 320ms to 85ms.
- Designed relational schemas and query optimizations in PostgreSQL, managing datasets over 10TB.
- Automated CI/CD deployment pipelines using GitHub Actions targeting AWS ECS.

Software Engineer | FinFlow Systems (2020 - 2022)
- Built financial transaction processing services with Python, Django, and PostgreSQL.
- Conducted unit and integration testing with pytest, achieving 92% code coverage.
- Integrated third-party payment gateways and secured endpoints using OAuth2 and JWT.

EDUCATION
B.S. in Computer Science | State University (Graduated Magna Cum Laude)
"""

# Preset Job Descriptions for Fast Testing
JOB_PRESETS: Dict[str, str] = {
    "Senior Python Backend Engineer": """Role: Senior Backend Engineer (Python / Microservices)
Company: Nexus Cloud Innovations
Location: Remote

ABOUT THE ROLE:
Nexus Cloud Innovations is looking for an experienced Senior Backend Engineer to join our core platform team. You will lead the design, implementation, and scaling of mission-critical cloud-native microservices processing millions of events daily.

KEY RESPONSIBILITIES:
- Design, build, and maintain high-performance asynchronous RESTful APIs and event-driven services using Python and FastAPI.
- Scale containerized infrastructure using Docker and Kubernetes on AWS cloud environments.
- Integrate message queues and event streaming platforms using Apache Kafka and Redis.
- Collaborate with DevOps engineers to implement robust CI/CD pipelines, automated testing with pytest, and Infrastructure as Code with Terraform.
- Optimize database performance and write advanced queries in PostgreSQL.

MINIMUM REQUIREMENTS:
- 4+ years of professional backend software engineering experience with Python.
- Deep expertise with web frameworks like FastAPI, Flask, or Django.
- Hands-on experience with containerization (Docker) and container orchestration (Kubernetes).
- Strong relational database experience with PostgreSQL, indexing, and schema design.
- Practical experience with cloud services (AWS: EC2, S3, EKS, RDS).
- Familiarity with event streaming and caching systems like Kafka and Redis.
- Solid background in automated unit testing (pytest) and CI/CD pipelines.
""",
    "Machine Learning & AI Engineer": """Role: Machine Learning Engineer (NLP / LLMs)
Company: Cognitive AI Labs
Location: Hybrid

ABOUT THE ROLE:
We are seeking an ambitious Machine Learning Engineer to scale our production AI models. You will design, train, and deploy transformer-based NLP and LLM systems integrated with real-time web services.

REQUIREMENTS:
- Proficient in Python, PyTorch, Scikit-learn, and HuggingFace transformers.
- Experience building production inference APIs using FastAPI and Docker.
- Working knowledge of vector databases, Redis, and PostgreSQL.
- Solid background in data processing using Pandas and NumPy.
- Familiarity with cloud platforms (AWS, GCP) and CI/CD automation.
- Understanding of distributed systems and ML model monitoring.
""",
    "Full-Stack React & Node Engineer": """Role: Full-Stack Software Engineer (React / TypeScript / Node)
Company: Elevate Web Solutions
Location: Remote

REQUIREMENTS:
- 3+ years experience with modern JavaScript / TypeScript.
- Strong UI engineering skills with React, Next.js, HTML5, CSS3, and Tailwind CSS.
- Backend API development experience using Node.js, Express, or NestJS.
- Experience with relational and NoSQL databases like PostgreSQL and MongoDB.
- Containerization with Docker and deployment pipelines on AWS or Vercel.
- Passion for writing clean, tested code with Jest and Git version control.
""",
}

SAMPLE_JOB_DESCRIPTION = JOB_PRESETS["Senior Python Backend Engineer"]
