import pandas as pd


def build_segment_churn_table(
    df: pd.DataFrame,
    index_cols: list[str],
    column_col: str,
    target_col: str = "Churn",
    empty_label: str = "—",
    small_n_threshold: int | None = None,
) -> pd.DataFrame:
    """
    Build a formatted segment churn table showing:
    churn rate (churned_count / total_count)

    Example cell:
        70.2% (643/916)

    Parameters
    ----------
    df : pd.DataFrame
        Source dataframe.
    index_cols : list[str]
        Columns to use as row index in the crosstab.
    column_col : str
        Column to use as crosstab columns.
    target_col : str, default="Churn"
        Binary target column where 1 = churn and 0 = no churn.
    empty_label : str, default="—"
        Label used when a segment has zero observations.
    small_n_threshold : int | None, default=None
        If provided, add '*' to cells where total count is below this threshold.

    Returns
    -------
    pd.DataFrame
        Formatted table with strings like '70.2% (643/916)'.
    """

    rate_table = pd.crosstab(
        [df[col] for col in index_cols],
        df[column_col],
        values=df[target_col],
        aggfunc="mean"
    )

    total_table = pd.crosstab(
        [df[col] for col in index_cols],
        df[column_col]
    )

    churned_table = pd.crosstab(
        [df[col] for col in index_cols],
        df[column_col],
        values=df[target_col],
        aggfunc="sum"
    )

    combined_table = total_table.copy().astype(object)

    for row in combined_table.index:
        for col in combined_table.columns:
            total = total_table.loc[row, col]

            if total == 0:
                combined_table.loc[row, col] = empty_label
                continue

            rate = rate_table.loc[row, col]
            churned = churned_table.loc[row, col]

            cell = f"{rate:.1%} ({int(churned)}/{int(total)})"

            if small_n_threshold is not None and total < small_n_threshold:
                cell += "*"

            combined_table.loc[row, col] = cell

    return combined_table