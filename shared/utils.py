"""
TalentBridge AI - Shared Utilities
Reusable UI components, banners, error handlers, and module loaders.
Designed to ensure visual consistency across all 12 modules without tight coupling.
"""

import importlib
import traceback
from typing import Callable, Optional, Sequence


def render_module_header(
    title: str,
    member: str,
    description: str,
    badge: str = "Active Baseline",
    badge_color: str = "#22c55e",
) -> None:
    """
    Renders a unified, premium header banner for any module.
    """
    import streamlit as st

    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
                    padding: 1.5rem; border-radius: 12px; margin-bottom: 1.5rem;
                    border: 1px solid #334155; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem;">
                <h2 style="color: #f8fafc; margin: 0; font-weight: 700; font-size: 1.6rem;">{title}</h2>
                <span style="background-color: {badge_color}22; color: {badge_color};
                             border: 1px solid {badge_color}; padding: 0.25rem 0.75rem;
                             border-radius: 9999px; font-size: 0.8rem; font-weight: 600; text-transform: uppercase;">
                    {badge}
                </span>
            </div>
            <p style="color: #94a3b8; margin-top: 0.5rem; margin-bottom: 0.25rem; font-size: 0.95rem;">
                {description}
            </p>
            <div style="color: #38bdf8; font-size: 0.85rem; font-weight: 500; margin-top: 0.5rem;">
                👤 <strong>Assigned Lead:</strong> {member}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_disclaimer(
    custom_message: Optional[str] = None,
) -> None:
    """
    Renders an ethical AI disclaimer explicitly stating that ML metrics
    are analytical guidance and not deterministic hiring or academic decisions.
    """
    import streamlit as st

    default_msg = (
        "<strong>Notice & Ethical Disclaimer:</strong> Machine Learning metrics (such as text similarity, "
        "relevance scores, or predictive ratings) are decision-support heuristics. A high similarity score "
        "indicates textual and keyword alignment with the target description; it is <strong>not</strong> "
        "a guarantee or probability of employment, hiring, or admission. Final evaluations must always involve "
        "holistic human review."
    )
    msg = custom_message if custom_message else default_msg

    st.markdown(
        f"""
        <div style="background-color: #fffbeb; border-left: 4px solid #f59e0b;
                    padding: 0.9rem 1.1rem; border-radius: 6px; margin: 1.25rem 0;
                    color: #92400e; font-size: 0.88rem; line-height: 1.45;">
            {msg}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_placeholder(
    module_key: str,
    module_title: str,
    member_name: str,
    expected_inputs: Sequence[str],
    expected_outputs: Sequence[str],
    suggested_models: Optional[Sequence[str]] = None,
) -> None:
    """
    Renders a structured, interactive placeholder interface for upcoming modules.
    Guides assigned team members on where to insert their implementation.
    """
    import streamlit as st

    render_module_header(
        title=module_title,
        member=member_name,
        description=f"Independent ML module scaffold for {module_title}. Ready for algorithm development.",
        badge="In Development",
        badge_color="#f59e0b",
    )

    st.info(
        f"🚧 **Module Scaffolding Active**: This module is assigned to **{member_name}**. "
        f"The isolated folder structure is prepared under `modules/{module_key}/`. "
        "Follow the checklist below to complete your algorithm implementation."
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📥 Expected Inputs")
        for item in expected_inputs:
            st.markdown(f"- {item}")

    with col2:
        st.markdown("### 📤 Expected Outputs")
        for item in expected_outputs:
            st.markdown(f"- {item}")

    if suggested_models:
        st.markdown("### 🧠 Suggested ML Architectures & Algorithms")
        for model in suggested_models:
            st.markdown(f"- `{model}`")

    st.markdown("---")
    st.markdown("### 🛠️ Developer Checklist for Module Owner")
    st.markdown(
        f"""
        1. Navigate to: `modules/{module_key}/`
        2. Place training datasets in `modules/{module_key}/data/` (or run a synthetic generator).
        3. Define data cleaning and feature engineering in `modules/{module_key}/preprocessing.py` (optional).
        4. Implement your model pipeline in `modules/{module_key}/model.py`.
        5. Build the user-facing Streamlit controls in `modules/{module_key}/interface.py` inside `render()`.
        6. Add unit tests inside `modules/{module_key}/tests/`.
        7. Update `modules/{module_key}/README.md` with your dataset and model metrics.
        """
    )

    render_disclaimer()


def safe_import_render(module_path: str) -> Optional[Callable[[], None]]:
    """
    Safely imports the `render()` callable from a module path (e.g. 'modules.fake_job_detection.interface').
    Catches and formats import errors without crashing the main application.
    """
    try:
        mod = importlib.import_module(module_path)
        render_fn = getattr(mod, "render", None)
        if render_fn is None or not callable(render_fn):
            raise AttributeError(f"Module '{module_path}' does not define a callable 'render()' function.")
        return render_fn
    except Exception as exc:
        import streamlit as st

        st.error(
            f"❌ **Failed to load module `{module_path}`**: {str(exc)}"
        )
        with st.expander("Show Traceback Details"):
            st.code(traceback.format_exc(), language="python")
        return None
