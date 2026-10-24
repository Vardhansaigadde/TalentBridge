"""
TalentBridge AI - Resume–Job Matching Interface
Streamlit user interface for Member 1's ML use case.
"""

import streamlit as st

from shared.utils import render_disclaimer, render_module_header
from .config import SAMPLE_JOB_DESCRIPTION, SAMPLE_RESUME
from .model import ResumeJobMatcher


def render() -> None:
    """
    Renders the interactive Streamlit user interface for Resume–Job Matching.
    Adheres to the platform interface contract.
    """
    render_module_header(
        title="Resume–Job Matching Engine",
        member="Member 1 (Lead)",
        description=(
            "Calculates semantic similarity and keyword alignment between candidate resumes "
            "and job descriptions using TF-IDF vectorization and cosine similarity."
        ),
        badge="Active Baseline",
        badge_color="#22c55e",
    )

    # Initialize session state for pre-filling sample text
    if "rjm_resume_input" not in st.session_state:
        st.session_state["rjm_resume_input"] = SAMPLE_RESUME
    if "rjm_job_input" not in st.session_state:
        st.session_state["rjm_job_input"] = SAMPLE_JOB_DESCRIPTION

    col_btn1, col_btn2, _ = st.columns([1.5, 1.5, 3])
    with col_btn1:
        if st.button("📋 Load Sample Data", use_container_width=True, help="Load realistic sample resume and job description"):
            st.session_state["rjm_resume_input"] = SAMPLE_RESUME
            st.session_state["rjm_job_input"] = SAMPLE_JOB_DESCRIPTION
            st.rerun()

    with col_btn2:
        if st.button("🧹 Clear Inputs", use_container_width=True, help="Reset text areas to empty"):
            st.session_state["rjm_resume_input"] = ""
            st.session_state["rjm_job_input"] = ""
            st.rerun()

    # Input Columns for Resume & Job Description
    col_resume, col_job = st.columns(2)

    with col_resume:
        st.markdown("#### 📄 Candidate Resume")
        resume_text = st.text_area(
            label="Paste Candidate Resume Text",
            value=st.session_state["rjm_resume_input"],
            height=320,
            placeholder="Paste raw resume text, CV sections, or project descriptions here...",
            key="resume_textarea",
            help="Plain text input of the candidate's resume or curriculum vitae.",
        )

    with col_job:
        st.markdown("#### 💼 Target Job Description")
        job_text = st.text_area(
            label="Paste Job Description / Requirements",
            value=st.session_state["rjm_job_input"],
            height=320,
            placeholder="Paste full job posting, key responsibilities, and technical requirements here...",
            key="job_textarea",
            help="Plain text input of the vacancy requirements.",
        )

    st.markdown("<br>", unsafe_allow_html=True)
    match_clicked = st.button("⚡ Match Resume to Job", type="primary", use_container_width=True)

    if match_clicked:
        if not resume_text.strip() or not job_text.strip():
            st.warning("⚠️ Please provide both a Resume and a Job Description before matching.")
            return

        with st.spinner("Analyzing text representations and computing TF-IDF similarity..."):
            # Load or initialize matcher
            matcher = ResumeJobMatcher.load()
            results = matcher.predict(resume_text=resume_text, job_text=job_text)

        st.markdown("---")
        st.markdown("### 📊 Matching Analytics & Results")

        # Top Metric Cards
        metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

        with metric_col1:
            st.metric(
                label="Similarity Score",
                value=f"{results['match_percentage']}%",
                help="Cosine similarity mapped to percentage [0% - 100%]"
            )

        with metric_col2:
            st.metric(
                label="Match Classification",
                value=results["match_level"],
                help="Threshold: High (>=70%), Moderate (40-69%), Low (<40%)"
            )

        with metric_col3:
            st.metric(
                label="Matched Keywords",
                value=f"{len(results['matched_keywords'])} skills",
                help="Key technical terms from JD found in resume"
            )

        with metric_col4:
            st.metric(
                label="Missing Keywords",
                value=f"{len(results['missing_keywords'])} gaps",
                help="Important terms from JD not identified in resume"
            )

        # Visual progress bar
        norm_score = float(results["similarity_score"])
        st.progress(norm_score, text=f"Textual Alignment: {results['match_percentage']}%")

        # Summary box
        st.markdown(
            f"""
            <div style="background-color: #f8fafc; border-left: 4px solid {results['match_color']};
                        padding: 0.8rem 1rem; border-radius: 6px; margin: 1rem 0; color: #1e293b;">
                <strong>Evaluation:</strong> {results['verdict']}
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Keyword Breakdown Columns
        res_col1, res_col2 = st.columns(2)

        with res_col1:
            st.markdown("#### ✅ Matched Skills & Keywords")
            if results["matched_keywords"]:
                pills_html = " ".join(
                    [
                        f"<span style='background-color: #dcfce7; color: #166534; padding: 4px 10px; "
                        f"border-radius: 12px; font-size: 0.82rem; margin: 3px; display: inline-block;'>"
                        f"✓ {kw}</span>"
                        for kw in results["matched_keywords"]
                    ]
                )
                st.markdown(pills_html, unsafe_allow_html=True)
            else:
                st.info("No significant common keywords identified.")

        with res_col2:
            st.markdown("#### ⚠️ Skill Gaps & Missing Keywords")
            if results["missing_keywords"]:
                pills_html = " ".join(
                    [
                        f"<span style='background-color: #fee2e2; color: #991b1b; padding: 4px 10px; "
                        f"border-radius: 12px; font-size: 0.82rem; margin: 3px; display: inline-block;'>"
                        f"✗ {kw}</span>"
                        for kw in results["missing_keywords"]
                    ]
                )
                st.markdown(pills_html, unsafe_allow_html=True)
            else:
                st.success("Excellent coverage! No prominent keywords from the job description are missing.")

        # Document Stats Expander
        with st.expander("🔍 View Text Processing Diagnostics"):
            st.write(
                {
                    "Resume Word Count": results["resume_word_count"],
                    "Job Description Word Count": results["job_word_count"],
                    "Top 15 Extracted Job Keywords": results["top_job_keywords"][:15],
                    "Raw Cosine Similarity": round(results["similarity_score"], 4),
                }
            )

    # Mandatory Ethical Disclaimer
    render_disclaimer(
        custom_message=(
            "<strong>Crucial Note:</strong> The similarity score represents <em>textual and keyword alignment</em> "
            "between the submitted resume and job description calculated via Term Frequency-Inverse Document Frequency "
            "(TF-IDF) and Cosine Distance. <strong>It is NOT a probability of being hired or an endorsement of candidate quality.</strong> "
            "Real-world hiring decisions evaluate candidate potential, soft skills, problem-solving abilities, and culture fit."
        )
    )
