from pathlib import Path

# -------------------------
# Project paths
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "clean"
PROCESSED_DATA_DASHBOARD_DIR = DATA_DIR / "dashboard"
# -------------------------
# File locations
# -------------------------
CHURN_RAW_FILE = RAW_DATA_DIR / "Telco_Churn_Dataset.csv"
CHURN_CLEAN_DASHBOARD_FILE = PROCESSED_DATA_DASHBOARD_DIR/ "teleco_churn_clean_dashboard.csv"
CHURN_CLEAN_FILE = PROCESSED_DATA_DIR / "teleco_churn_clean.csv"

