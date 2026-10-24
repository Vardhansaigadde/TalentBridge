"""
TalentBridge AI - Production Resume–Job Matching User Interface.
Supports PDF/DOCX/TXT uploads, domain skills taxonomy breakdown, and ATS optimization audits.
"""

import streamlit as st

from shared.utils import render_disclaimer, render_module_header
from .config import JOB_PRESETS, SAMPLE_JOB_DESCRIPTION, SAMPLE_RESUME
from .model import ResumeJobMatcher
from .preprocessing import parse_document


def render() -> None:
    """
    Renders the interactive Streamlit user interface for Resume–Job Matching.
    Adheres strictly to the TalentBridge AI interface contract.
    """
    render_module_header(
        title="Resume–Job Matching Engine",
        member="Member 1 (Lead)",
        description=(
            "Hybrid talent intelligence engine analyzing document resumes (PDF, DOCX, TXT), "
            "domain skills taxonomy alignment, and ATS readiness optimization."
        ),
        badge="Production Ready",
        badge_color="#22c55e",
    )

    # Session State Initialization
    if "active_resume_text" not in st.session_state:
        st.session_state["active_resume_text"] = SAMPLE_RESUME
    if "active_job_text" not in st.session_state:
        st.session_state["active_job_text"] = SAMPLE_JOB_DESCRIPTION

    # Top Controls: Preset selector and quick resets
    control_c1, control_c2, control_c3 = st.columns([2.5, 1.2, 1.2])

    with control_c1:
        preset_names = list(JOB_PRESETS.keys()) + ["Custom Job Description"]
        selected_preset = st.selectbox(
            "💼 Select Target Job Role Preset:",
            options=preset_names,
            index=0,
            help="Choose a pre-configured technical job description or enter your own custom text."
        )
        if selected_preset in JOB_PRESETS:
            st.session_state["active_job_text"] = JOB_PRESETS[selected_preset]

    with control_c2:
        st.write("")
        st.write("")
        if st.button("📋 Load Sample Data", use_container_width=True):
            st.session_state["active_resume_text"] = SAMPLE_RESUME
            st.session_state["active_job_text"] = JOB_PRESETS["Senior Python Backend Engineer"]
            st.rerun()

    with control_c3:
        st.write("")
        st.write("")
        if st.button("🧹 Clear All", use_container_width=True):
            st.session_state["active_resume_text"] = ""
            st.session_state["active_job_text"] = ""
            st.rerun()

    # Input Columns: Resume Ingestion & Job Posting
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("### 📄 1. Candidate Resume")
        tab_upload, tab_paste = st.tabs(["📁 Upload File (PDF / DOCX / TXT)", "✍️ Paste Resume Text"])

        with tab_upload:
            uploaded_file = st.file_uploader(
                label="Choose a resume file",
                type=["pdf", "docx", "doc", "txt"],
                help="Supports modern PDF, Microsoft Word (.docx), or plain text resume documents."
            )
            if uploaded_file is not None:
                try:
                    with st.spinner("Extracting text and structure from uploaded document..."):
                        extracted_text = parse_document(uploaded_file, uploaded_file.name)
                        if extracted_text:
                            st.session_state["active_resume_text"] = extracted_text
                            st.success(
                                f"✅ Extracted **{len(extracted_text.split())} words** from `{uploaded_file.name}`"
                            )
                        else:
                            st.warning("Uploaded file appeared empty or could not be read.")
                except Exception as exc:
                    st.error(f"Failed to parse document: {str(exc)}")

            if st.session_state["active_resume_text"]:
                with st.expander("👁️ Preview Active Resume Text", expanded=False):
                    st.text(st.session_state["active_resume_text"][:800] + ("..." if len(st.session_state["active_resume_text"]) > 800 else ""))

        with tab_paste:
            pasted_resume = st.text_area(
                label="Raw Resume Text",
                value=st.session_state["active_resume_text"],
                height=300,
                key="resume_paste_box",
                placeholder="Paste candidate resume or CV text here...",
            )
            if pasted_resume != st.session_state["active_resume_text"]:
                st.session_state["active_resume_text"] = pasted_resume

    with col_right:
        st.markdown("### 💼 2. Target Job Description")
        job_text = st.text_area(
            label="Job Requirements & Technical Stack",
            value=st.session_state["active_job_text"],
            height=370,
            key="job_description_box",
            placeholder="Paste vacancy requirements, minimum qualifications, and tech stack here...",
        )
        if job_text != st.session_state["active_job_text"]:
            st.session_state["active_job_text"] = job_text

    st.markdown("<br>", unsafe_allow_html=True)
    match_btn = st.button("⚡ Run Resume–Job Matching Analysis", type="primary", use_container_width=True)

    # Execution & Results
    if match_btn:
        active_resume = st.session_state["active_resume_text"].strip()
        active_job = st.session_state["active_job_text"].strip()

        if not active_resume or not active_job:
            st.warning("⚠️ Please provide both a Resume and a Job Description before matching.")
            return

        with st.spinner("Executing hybrid matching (TF-IDF + Domain Skills Taxonomy + ATS Audit)..."):
            matcher = ResumeJobMatcher.load()
            results = matcher.predict(resume_text=active_resume, job_text=active_job)

        st.markdown("---")
        st.markdown("## 📊 Comprehensive Matching Results")

        # Top 4 KPI Metrics
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.metric(
                label="Overall Match Score",
                value=f"{results['match_percentage']}%",
                help="Composite metric combining technical skills overlap (55%) and TF-IDF similarity (45%)."
            )
        with m2:
            st.metric(
                label="Skills Coverage",
                value=f"{results['skills_overlap_percentage']}%",
                help="Percentage of technical skills required in the job description found on the resume."
            )
        with m3:
            st.metric(
                label="Textual Alignment",
                value=f"{results['textual_similarity_percentage']}%",
                help="Cosine similarity across vocabulary, context, and experience descriptions."
            )
        with m4:
            st.metric(
                label="Classification Tier",
                value=results["match_level"],
                help="High (>=75%), Moderate (45-74%), Low (<45%)"
            )

        # Visual progress bar
        st.progress(float(results["similarity_score"]), text=f"Composite Suitability: {results['match_percentage']}%")

        # Verdict notification banner
        st.markdown(
            f"""
            <div style="background-color: #f8fafc; border-left: 4px solid {results['match_color']};
                        padding: 0.9rem 1.1rem; border-radius: 8px; margin: 1.25rem 0; color: #0f172a;">
                <h4 style="margin: 0; color: {results['match_color']};">{results['match_level']}</h4>
                <p style="margin: 0.35rem 0 0 0; font-size: 0.93rem;">{results['verdict']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Tabbed Deep-Dive Analytics
        tab_skills, tab_ats, tab_action = st.tabs([
            "🎯 Skills Taxonomy & Gap Breakdown",
            "📝 ATS Readiness & Impact Diagnostics",
            "🚀 Step-by-Step Optimization Plan",
        ])

        # ----------------------------------------------------------------------
        # Tab A: Skills Gap Breakdown
        # ----------------------------------------------------------------------
        with tab_skills:
            st.markdown("#### Technical Competencies by Category")
            category_breakdown = results["category_breakdown"]

            cat_cols = st.columns(3)
            categories = list(category_breakdown.keys())

            for i, cat in enumerate(categories):
                col = cat_cols[i % 3]
                data = category_breakdown[cat]
                with col:
                    st.markdown(
                        f"""
                        <div style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 0.9rem; margin-bottom: 1rem; background-color: #ffffff;">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <strong style="font-size: 0.92rem; color: #1e293b;">{cat}</strong>
                                <span style="font-size: 0.8rem; font-weight: 600; color: {'#16a34a' if data['coverage_percent'] >= 60 else '#ea580c'};">
                                    {data['matched_count']}/{data['required_count']} ({data['coverage_percent']}%)
                                </span>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    if data["matched"]:
                        st.caption("✅ Matched: " + ", ".join(data["matched"]))
                    if data["missing"]:
                        st.caption("❌ Missing: " + ", ".join(data["missing"]))

            st.markdown("---")
            skill_c1, skill_c2 = st.columns(2)

            with skill_c1:
                st.markdown("#### ✅ Matched Required Skills")
                if results["matched_keywords"]:
                    badges = "".join([
                        f"<span style='background-color: #dcfce7; color: #166534; padding: 4px 10px; "
                        f"border-radius: 12px; font-size: 0.82rem; margin: 3px; display: inline-block;'>"
                        f"✓ {s}</span>"
                        for s in results["matched_keywords"]
                    ])
                    st.markdown(badges, unsafe_allow_html=True)
                else:
                    st.info("No matching taxonomy skills identified.")

            with skill_c2:
                st.markdown("#### ❌ Critical Skill Gaps (In JD but Not on Resume)")
                if results["missing_keywords"]:
                    badges = "".join([
                        f"<span style='background-color: #fee2e2; color: #991b1b; padding: 4px 10px; "
                        f"border-radius: 12px; font-size: 0.82rem; margin: 3px; display: inline-block;'>"
                        f"✗ {s}</span>"
                        for s in results["missing_keywords"]
                    ])
                    st.markdown(badges, unsafe_allow_html=True)
                else:
                    st.success("🎉 Superb! All technical competencies specified in the job are present on the resume.")

            if results["bonus_skills"]:
                with st.expander("✨ Candidate Additional Skills (Bonus Competencies)"):
                    st.markdown(
                        ", ".join(f"`{s}`" for s in results["bonus_skills"][:20])
                        + ("..." if len(results["bonus_skills"]) > 20 else "")
                    )

        # ----------------------------------------------------------------------
        # Tab B: ATS Diagnostics
        # ----------------------------------------------------------------------
        with tab_ats:
            ats = results["ats_audit"]
            st.markdown("#### Applicant Tracking System (ATS) Structural Audit")

            ats_c1, ats_c2, ats_c3, ats_c4 = st.columns(4)
            with ats_c1:
                st.metric(label="Resume Length", value=f"{ats['word_count']} words", delta=ats["length_status"])
            with ats_c2:
                st.metric(label="Standard Sections", value=f"{len(ats['sections_present'])} / 5 Detected")
            with ats_c3:
                st.metric(label="Strong Action Verbs", value=f"{ats['action_verb_count']} found")
            with ats_c4:
                st.metric(label="Quantified Metrics", value=f"{ats['quantification_count']} metrics")

            st.markdown("---")
            sec_col1, sec_col2 = st.columns(2)

            with sec_col1:
                st.markdown("##### 📑 Section Headers Checklist")
                for sec in ["Contact Info", "Professional Experience", "Education", "Skills", "Projects"]:
                    if sec in ats["sections_present"]:
                        st.markdown(f"- ✅ **{sec}**: Detected")
                    else:
                        st.markdown(f"- ⚠️ **{sec}**: *Missing or non-standard heading*")

            with sec_col2:
                st.markdown("##### 💥 Strong Action Verbs Identified")
                if ats["action_verbs_found"]:
                    st.write(", ".join(f"`{v}`" for v in ats["action_verbs_found"][:15]))
                else:
                    st.warning("Few or no strong action verbs detected. Upgrade passive bullet points.")

        # ----------------------------------------------------------------------
        # Tab C: Action Plan
        # ----------------------------------------------------------------------
        with tab_action:
            st.markdown("#### 🚀 Actionable Strategy to Maximize Match Rate")
            for idx, plan_item in enumerate(results["optimization_plan"], 1):
                st.markdown(f"**{idx}.** {plan_item}")

    # Ethical AI Disclaimer
    render_disclaimer(
        custom_message=(
            "<strong>Notice & Ethical AI Disclaimer:</strong> The Resume–Job Matching score is a mathematical "
            "representation of semantic and keyword alignment calculated via TF-IDF vectorization and domain taxonomy overlap. "
            "<strong>It is NOT a probability of being hired or an endorsement of employment.</strong> "
            "Holistic human evaluation considering cultural values, problem solving, teamwork, and code reviews must always govern talent decisions."
        )
    )
