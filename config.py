import sys
import logging
from pathlib import Path

import matplotlib as mpl


# --- 1. DYNAMIC PATH DISCOVERY ---
ROOT_DIR = Path(__file__).resolve().parent
RESULTS_DIR = ROOT_DIR / "results"


# --- 2. SYSTEM REGISTRATION ---
# Register root directory to prevent import duplication and prioritize project modules
if str(ROOT_DIR) not in sys.path: 
    sys.path.insert(0, str(ROOT_DIR))

# Register legacy script folders for backward compatibility
LEGACY_SCRIPTS_DIR = ROOT_DIR / "legacy" / "old_scripts"
if LEGACY_SCRIPTS_DIR.exists() and str(LEGACY_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(LEGACY_SCRIPTS_DIR))


# --- 3. GLOBAL CONSTANTS ---
TDA_RES = 100


# --- 4. PLOTTING & STYLING ---
def apply_plot_settings():
    """Apply consistent visual styles to all plots in the project."""
    mpl.rcParams['font.family'] = 'sans-serif'
    mpl.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'Liberation Sans', 'sans-serif']
    
    # Silence matplotlib font manager warnings to keep terminal clean
    logging.getLogger('matplotlib.font_manager').setLevel(logging.ERROR)


# --- 5. DATA UTILITIES ---
def get_mat_files():
    """
    Recursively find all .mat files in the project.
    Filters out files in ignored directories (e.g., .venv, results).
    """
    ignored_dirs = {'.venv', 'site-packages', 'results', '__pycache__'}
    
    # Using p.parts safely checks actual folder names rather than substrings
    return [
        str(p) for p in ROOT_DIR.rglob("*.mat")
        if not any(ignored in p.parts for ignored in ignored_dirs)
    ]

def get_output_dir(name: str) -> Path:
    """
    Create and return a specific subfolder inside the 'results' directory.
    
    Usage:
        BASE_OUT_DIR = config.get_output_dir("topo_feats")
    """
    path = RESULTS_DIR / name
    path.mkdir(parents=True, exist_ok=True)
    return path