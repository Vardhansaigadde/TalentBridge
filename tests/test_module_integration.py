"""
TalentBridge AI - Platform Integration Tests
Validates the architecture, folder structure, contract compliance,
and registry integrity for all 12 modules.
"""

import importlib
import sys
from pathlib import Path
from typing import List
import pytest

# Ensure project root is on sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# All 12 assigned module identifiers
EXPECTED_MODULES: List[str] = [
    "resume_job_matching",
    "fake_job_detection",
    "student_performance",
    "entrance_exam_prediction",
    "placement_risk",
    "interview_analyzer",
    "learning_difficulty",
    "fairness_recruitment",
    "employee_attrition",
    "resume_analyzer",
    "internship_fraud_detection",
    "personalized_learning",
]


def test_all_12_module_directories_exist():
    """Verify that each of the 12 assigned module directories exists under modules/."""
    modules_dir = PROJECT_ROOT / "modules"
    assert modules_dir.is_dir(), "The 'modules/' directory must exist."

    for mod_name in EXPECTED_MODULES:
        mod_path = modules_dir / mod_name
        assert mod_path.is_dir(), f"Expected module folder does not exist: {mod_path}"


def test_required_files_in_each_module():
    """
    Verify that every module has the required files:
    __init__.py, interface.py, model.py, README.md, data/.gitkeep, artifacts/.gitkeep, tests/.
    """
    modules_dir = PROJECT_ROOT / "modules"

    for mod_name in EXPECTED_MODULES:
        mod_path = modules_dir / mod_name
        assert (mod_path / "__init__.py").is_file(), f"{mod_name} missing __init__.py"
        assert (mod_path / "interface.py").is_file(), f"{mod_name} missing interface.py"
        assert (mod_path / "model.py").is_file(), f"{mod_name} missing model.py"
        assert (mod_path / "README.md").is_file(), f"{mod_name} missing README.md"
        assert (mod_path / "data" / ".gitkeep").is_file(), f"{mod_name} missing data/.gitkeep"
        assert (mod_path / "artifacts" / ".gitkeep").is_file(), f"{mod_name} missing artifacts/.gitkeep"
        assert (mod_path / "tests").is_dir(), f"{mod_name} missing tests directory"


def test_member_1_complete_structure():
    """Verify that Member 1's resume_job_matching has all specialized files."""
    rjm_dir = PROJECT_ROOT / "modules" / "resume_job_matching"
    assert (rjm_dir / "preprocessing.py").is_file(), "resume_job_matching missing preprocessing.py"
    assert (rjm_dir / "config.py").is_file(), "resume_job_matching missing config.py"
    assert (rjm_dir / "train.py").is_file(), "resume_job_matching missing train.py"
    assert (rjm_dir / "tests" / "test_resume_job_matching.py").is_file(), (
        "resume_job_matching missing test_resume_job_matching.py"
    )


def test_all_modules_satisfy_render_contract():
    """
    Verify that every one of the 12 modules exposes a callable render() function in interface.py.
    """
    for mod_name in EXPECTED_MODULES:
        interface_import_path = f"modules.{mod_name}.interface"
        mod = importlib.import_module(interface_import_path)
        assert hasattr(mod, "render"), f"{interface_import_path} must define a 'render()' function."
        assert callable(getattr(mod, "render")), f"{interface_import_path}.render must be a callable."


def test_app_module_registry():
    """Verify that app.py contains a complete registry covering all 12 modules."""
    import app

    registry_module_ids = [m["id"] for m in app.MODULE_REGISTRY if m["id"] != "overview"]

    # Check length
    assert len(registry_module_ids) == 12, (
        f"Registry should have 12 ML modules, found {len(registry_module_ids)}"
    )

    # Check all expected IDs are registered
    for expected_id in EXPECTED_MODULES:
        assert expected_id in registry_module_ids, f"Module '{expected_id}' not found in app.py MODULE_REGISTRY"

    # Verify each module path points to a valid interface
    for entry in app.MODULE_REGISTRY:
        if entry["id"] == "overview":
            continue
        mod_path = entry["module_path"]
        assert mod_path is not None, f"Module path cannot be None for {entry['id']}"
        imported = importlib.import_module(mod_path)
        assert hasattr(imported, "render"), f"{mod_path} must expose 'render()'"


def test_shared_utils_import():
    """Verify that shared utilities import cleanly and define expected helpers."""
    import shared.utils as utils

    assert hasattr(utils, "render_module_header")
    assert hasattr(utils, "render_disclaimer")
    assert hasattr(utils, "render_placeholder")
    assert hasattr(utils, "safe_import_render")
