"""
Configuration settings, constants, and sample test data for Resume–Job Matching.
"""

from pathlib import Path

# Paths
MODULE_DIR = Path(__file__).resolve().parent
DATA_DIR = MODULE_DIR / "data"
ARTIFACTS_DIR = MODULE_DIR / "artifacts"
MODEL_PATH = ARTIFACTS_DIR / "tfidf_vectorizer.joblib"

# Model Parameters
TFIDF_MAX_FEATURES = 5000
TFIDF_NGRAM_RANGE = (1, 2)
SUBLINEAR_TF = True

# Score Categorization Thresholds (in percentage)
THRESHOLD_HIGH = 70.0
THRESHOLD_MODERATE = 40.0

# Curated Technical Domain Stopwords / Noise Words to filter from keyword analysis
ADDITIONAL_STOPWORDS = {
    "responsibilities", "requirements", "experience", "years", "candidate", "role",
    "team", "work", "working", "looking", "plus", "skills", "ability", "strong",
    "good", "excellent", "knowledge", "required", "preferred", "must", "have",
    "including", "opportunity", "company", "position", "demonstrated", "familiarity"
}

# Default Sample Resume (Tech/Software Engineering profile)
SAMPLE_RESUME = """Jane Doe
Senior Python Backend Developer | Distributed Systems & Cloud
Email: jane.doe@example.com | GitHub: github.com/janedoe | LinkedIn: linkedin.com/in/janedoe

PROFESSIONAL SUMMARY
Results-driven software engineer with 5+ years of experience building high-throughput microservices, REST APIs, and data pipelines using Python, FastAPI, and Docker. Proven track record of improving database query performance by 40% and deploying scalable containerized applications on AWS.

CORE TECHNICAL SKILLS
- Languages: Python, SQL, Bash, JavaScript
- Frameworks & Libraries: FastAPI, Flask, Django, Pydantic, SQLAlchemy, Pandas, Scikit-learn
- Databases: PostgreSQL, MySQL, Redis
- Cloud & DevOps: AWS (EC2, S3, RDS), Docker, CI/CD (GitHub Actions), Git, Linux
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

# Default Sample Job Description (Backend / Cloud Role)
SAMPLE_JOB_DESCRIPTION = """Role: Senior Backend Engineer (Python / Microservices)
Company: Nexus Cloud Innovations
Location: Remote

ABOUT THE ROLE:
Nexus Cloud Innovations is looking for an experienced Senior Backend Engineer to join our core platform team. You will lead the design, implementation, and scaling of mission-critical cloud-native microservices processing millions of events daily.

KEY RESPONSIBILITIES:
- Design, build, and maintain high-performance asynchronous RESTful APIs and event-driven services using Python and FastAPI.
- Scale containerized infrastructure using Docker and Kubernetes on AWS cloud environments.
- Integrate message queues and event streaming platforms using Apache Kafka and Redis.
- Collaborate with DevOps engineers to implement robust CI/CD pipelines, automated testing with pytest, and Infrastructure as Code with Terraform.
- Optimize database performance and write advanced queries in PostgreSQL and distributed NoSQL databases.
- Participate in architectural design reviews, mentor junior developers, and ensure code quality and security standards.

MINIMUM REQUIREMENTS:
- 4+ years of professional backend software engineering experience with Python.
- Deep expertise with web frameworks like FastAPI, Flask, or Django.
- Hands-on experience with containerization (Docker) and container orchestration (Kubernetes).
- Strong relational database experience with PostgreSQL, indexing, and schema design.
- Practical experience with cloud services (AWS: EC2, S3, EKS, RDS).
- Familiarity with event streaming and caching systems like Kafka and Redis.
- Solid background in automated unit testing (pytest) and CI/CD pipelines.

NICE TO HAVE:
- Experience with Terraform or Infrastructure as Code.
- Knowledge of distributed tracing, Prometheus, and Grafana monitoring.
"""
