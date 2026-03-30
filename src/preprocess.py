import pandas as pd 

def prepare_model_data(df: pd.DataFrame, target_col: str = "Churn"):
    """
    Split dataframe into X and y and one-hot encode categorical features.
    Ensures:
    - Dummy variables are 0/1 integers
    - Column names contain no spaces (use underscores)
    """
    X = df.drop(columns=target_col).copy()
    y = df[target_col].copy()

    # Clean original column names
    X.columns = X.columns.str.replace(" ", "_")

    # One-hot encode
    X = pd.get_dummies(X, drop_first=True, dtype=int)

    # Clean any new dummy column names
    X.columns = X.columns.str.replace(" ", "_")

    return X, y