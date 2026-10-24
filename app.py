"""
TalentBridge AI - Integrated Machine Learning Platform
Central Streamlit Application & Dynamic Module Registry
"""

import importlib
import sys
import traceback
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

import streamlit as st

# Ensure project root is on Python path
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from shared.utils import render_disclaimer, render_module_header

# ==============================================================================
# Page Configuration
# ==============================================================================
st.set_page_config(
    page_title="TalentBridge AI",
    page_icon="🌉",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==============================================================================
# Maintainable Module Registry
# Defines all 12 independent ML use cases and their assigned owners.
# Future members can update this registry without altering core routing logic.
# ==============================================================================
MODULE_REGISTRY: List[Dict[str, Any]] = [
    {
        "id": "overview",
        "title": "Platform Overview & Team Dashboard",
        "member": "All Team Members",
        "category": "Platform",
        "icon": "🏠",
        "module_path": None,  # Rendered natively
        "status": "Production",
        "badge_color": "#38bdf8",
        "description": "Integrated architecture, 12-member use case matrix, and development guidelines.",
    },
    {
        "id": "resume_job_matching",
        "title": "Resume–Job Matching",
        "member": "Member 1 (Lead)",
        "category": "Talent Acquisition",
        "icon": "📄",
        "module_path": "modules.resume_job_matching.interface",
        "status": "Active Baseline",
        "badge_color": "#22c55e",
        "description": "TF-IDF & Cosine Similarity engine analyzing semantic overlap and candidate skill gaps.",
    },
    {
        "id": "fake_job_detection",
        "title": "Fake Job Posting Detection",
        "member": "Member 2",
        "category": "Trust & Safety",
        "icon": "🛡️",
        "module_path": "modules.fake_job_detection.interface",
        "status": "In Development",
        "badge_color": "#f59e0b",
        "description": "NLP classifier detecting fraudulent recruitment postings and scam signals.",
    },
    {
        "id": "student_performance",
        "title": "Student Performance Prediction",
        "member": "Member 3",
        "category": "Education Analytics",
        "icon": "📈",
        "module_path": "modules.student_performance.interface",
        "status": "In Development",
        "badge_color": "#f59e0b",
        "description": "Predictive regression modeling academic trajectory, GPA trends, and student risk.",
    },
    {
        "id": "entrance_exam_prediction",
        "title": "Entrance Examination Performance",
        "member": "Member 4",
        "category": "Education Analytics",
        "icon": "🎯",
        "module_path": "modules.entrance_exam_prediction.interface",
        "status": "In Development",
        "badge_color": "#f59e0b",
        "description": "Forecasts standardized exam percentiles and university admission feasibility.",
    },
    {
        "id": "placement_risk",
        "title": "Student Placement Risk Prediction",
        "member": "Member 5",
        "category": "Career Readiness",
        "icon": "⚠️",
        "module_path": "modules.placement_risk.interface",
        "status": "In Development",
        "badge_color": "#f59e0b",
        "description": "Identifies students requiring proactive career interventions before campus placements.",
    },
    {
        "id": "interview_analyzer",
        "title": "AI Interview Performance Analysis",
        "member": "Member 6",
        "category": "Career Readiness",
        "icon": "🎙️",
        "module_path": "modules.interview_analyzer.interface",
        "status": "In Development",
        "badge_color": "#f59e0b",
        "description": "Multimodal analysis of candidate interview transcripts, speech pace, and delivery.",
    },
    {
        "id": "learning_difficulty",
        "title": "Learning Difficulty Detection",
        "member": "Member 7",
        "category": "Adaptive Learning",
        "icon": "🧩",
        "module_path": "modules.learning_difficulty.interface",
        "status": "In Development",
        "badge_color": "#f59e0b",
        "description": "Real-time struggle detection and cognitive bottleneck identification in LMS modules.",
    },
    {
        "id": "fairness_recruitment",
        "title": "Fairness-Aware Recruitment",
        "member": "Member 8",
        "category": "Ethical AI",
        "icon": "⚖️",
        "module_path": "modules.fairness_recruitment.interface",
        "status": "In Development",
        "badge_color": "#f59e0b",
        "description": "Algorithmic bias audit evaluating demographic parity and disparate impact ratios.",
    },
    {
        "id": "employee_attrition",
        "title": "Employee Attrition Prediction",
        "member": "Member 9",
        "category": "Workforce Analytics",
        "icon": "🔄",
        "module_path": "modules.employee_attrition.interface",
        "status": "In Development",
        "badge_color": "#f59e0b",
        "description": "Retention modeling with explainable feature importance isolating turnover factors.",
    },
    {
        "id": "resume_analyzer",
        "title": "AI Resume Analysis",
        "member": "Member 10",
        "category": "Talent Acquisition",
        "icon": "🔍",
        "module_path": "modules.resume_analyzer.interface",
        "status": "In Development",
        "badge_color": "#f59e0b",
        "description": "Deep resume structure evaluation, quantification scoring, and ATS readiness checks.",
    },
    {
        "id": "internship_fraud_detection",
        "title": "Fake Internship Detection",
        "member": "Member 11",
        "category": "Trust & Safety",
        "icon": "🚨",
        "module_path": "modules.internship_fraud_detection.interface",
        "status": "In Development",
        "badge_color": "#f59e0b",
        "description": "Safeguards student applicants against deceptive, unpaid, or fee-charging internships.",
    },
    {
        "id": "personalized_learning",
        "title": "Personalized Learning Recommendations",
        "member": "Member 12",
        "category": "Adaptive Learning",
        "icon": "💡",
        "module_path": "modules.personalized_learning.interface",
        "status": "In Development",
        "badge_color": "#f59e0b",
        "description": "Curates custom skill-building pathways and courses matched to candidate gaps.",
    },
]


def load_module_render_fn(module_path: str) -> Optional[Callable[[], None]]:
    """
    Dynamically imports a module's render() function on demand.
    Avoids loading all 12 ML models into memory during initial app startup.
    """
    try:
        mod = importlib.import_module(module_path)
        render_fn = getattr(mod, "render", None)
        if not render_fn or not callable(render_fn):
            raise AttributeError(f"Module '{module_path}' has no callable 'render()' function.")
        return render_fn
    except Exception as exc:
        st.error(f"❌ **Error Loading Module (`{module_path}`)**")
        st.markdown(
            f"> **Exception:** `{type(exc).__name__}: {str(exc)}`\n\n"
            "This error has been captured safely. Please verify that all dependencies and "
            "module source files are present."
        )
        with st.expander("View Full Diagnostic Traceback", expanded=False):
            st.code(traceback.format_exc(), language="python")
        return None


def render_platform_overview() -> None:
    """
    Default landing dashboard showing project architecture, team roster, and quick status.
    """
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
                    padding: 2.2rem; border-radius: 14px; margin-bottom: 2rem;
                    border: 1px solid #334155; color: #f8fafc;">
            <div style="display: flex; align-items: center; gap: 1rem;">
                <span style="font-size: 2.8rem;">🌉</span>
                <div>
                    <h1 style="margin: 0; font-size: 2.2rem; font-weight: 800; color: #ffffff;">TalentBridge AI</h1>
                    <p style="margin: 0.3rem 0 0 0; color: #94a3b8; font-size: 1.05rem;">
                        Integrated Machine Learning Platform for Talent Intelligence & Career Development
                    </p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Top metrics
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Total Team Members", "12 Leads")
    with c2:
        st.metric("Machine Learning Modules", "12 Independent")
    with c3:
        st.metric("Active Working Baseline", "1 Module (Member 1)")
    with c4:
        st.metric("Scaffolds Prepared", "11 Modules")

    st.markdown("---")

    # Team Matrix Table
    st.markdown("### 📋 12-Member Use Case Matrix & Implementation Status")
    st.markdown(
        "Each team member develops within their dedicated module folder under `modules/` "
        "and exposes a `render()` function in `interface.py`."
    )

    modules_display = []
    for m in MODULE_REGISTRY:
        if m["id"] == "overview":
            continue
        modules_display.append({
            "Module Name": f"{m['icon']} {m['title']}",
            "Assigned Lead": m["member"],
            "Domain Category": m["category"],
            "Status": m["status"],
            "Directory": f"`modules/{m['id']}/`",
        })

    st.dataframe(modules_display, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.markdown("### 🚀 Architecture Principles for Team Members")

    arch_c1, arch_c2, arch_c3 = st.columns(3)
    with arch_c1:
        st.markdown(
            """
            #### 1. Strict Module Isolation
            - Every member owns their isolated folder: `modules/<module_name>/`.
            - Never modify code inside another member's folder.
            - All trained models, datasets, and tests live within your folder.
            """
        )
    with arch_c2:
        st.markdown(
            """
            #### 2. The `render()` Contract
            - In `modules/<your_module>/interface.py`, define:
            ```python
            def render() -> None:
                # Your UI & Model calls
                pass
            ```
            - `app.py` loads your module lazily when selected in the sidebar.
            """
        )
    with arch_c3:
        st.markdown(
            """
            #### 3. GitHub PR Workflow
            - Create branch: `feature/member-X-<usecase>`
            - Commit only files within your assigned module.
            - Run pytest integration checks before opening a pull request.
            """
        )

    render_disclaimer()


# ==============================================================================
# Sidebar Navigation & Execution
# ==============================================================================
def main() -> None:
    st.sidebar.markdown(
        """
        <div style="text-align: center; padding: 0.5rem 0 1rem 0;">
            <h2 style="margin: 0; color: #38bdf8;">🌉 TalentBridge AI</h2>
            <span style="font-size: 0.8rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px;">
                12-Member ML Platform
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Format list for radio buttons
    module_labels = [f"{m['icon']} {m['title']}" for m in MODULE_REGISTRY]
    selected_idx = st.sidebar.radio(
        label="Select Application Module:",
        options=range(len(MODULE_REGISTRY)),
        format_func=lambda i: module_labels[i],
        index=0,
    )

    selected_module = MODULE_REGISTRY[selected_idx]

    # Sidebar module meta info card
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**Current View:** {selected_module['icon']} {selected_module['title']}")
    st.sidebar.markdown(f"**Lead:** `{selected_module['member']}`")
    st.sidebar.markdown(f"**Category:** {selected_module['category']}")
    status_color = selected_module.get("badge_color", "#38bdf8")
    status_text = selected_module.get("status", "Active")
    st.sidebar.markdown(
        f"**Status:** <span style='color: {status_color}; font-weight: 600;'>{status_text}</span>",
        unsafe_allow_html=True,
    )

    st.sidebar.markdown("---")
    st.sidebar.caption("TalentBridge AI • Streamlit & Scikit-Learn Integration")

    # Render selected module or overview
    if selected_module["id"] == "overview":
        render_platform_overview()
    else:
        render_fn = load_module_render_fn(selected_module["module_path"])
        if render_fn:
            try:
                render_fn()
            except Exception as exc:
                st.error(
                    f"❌ **Runtime Execution Error in `{selected_module['title']}`**"
                )
                st.markdown(f"> `{type(exc).__name__}: {str(exc)}`")
                with st.expander("Diagnostic Stack Trace"):
                    st.code(traceback.format_exc(), language="python")


if __name__ == "__main__":
    main()
