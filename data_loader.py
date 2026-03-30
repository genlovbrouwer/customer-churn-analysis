import pandas as pd
from pathlib import Path

from src.config import CHURN_RAW_FILE


def load_csv(filepath: Path | str) -> pd.DataFrame:
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"Data file not found: {filepath}")
    return pd.read_csv(filepath)


def save_csv(df: pd.DataFrame, filepath: Path) -> None:
    """Save a DataFrame to CSV, creating parent directories if needed."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filepath, index=False)


def load_raw_churn_data() -> pd.DataFrame:
    """
    Load raw churn data from the configured file path.
    Expected columns: customerID,gender,SeniorCitizen,Partner,Dependents,tenure,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,MonthlyCharges,TotalCharges,Churn
    """
    return load_csv(CHURN_RAW_FILE)