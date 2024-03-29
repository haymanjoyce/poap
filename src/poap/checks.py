import pandas as pd
from typing import List


def check_column_labels(df: pd.DataFrame = None,
                        expected_labels: List[str] = None) -> None:
    """
    Checks the column labels of the provided DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame to check.
    expected_labels (List[str]): A list of expected column labels.

    Returns:
    None

    Raises:
    TypeError: If df is not a DataFrame or expected_labels is not a list.
    ValueError: If the DataFrame is empty or the column labels are not as expected.
    """
    if df is None:
        df = pd.DataFrame()
    if expected_labels is None:
        expected_labels = []

    if not isinstance(df, pd.DataFrame):
        raise TypeError("The provided object is not a DataFrame")
    if not isinstance(expected_labels, list):
        raise TypeError("'expected_labels' must be a list")
    if df.empty:
        raise ValueError("The DataFrame is empty")
    if list(df.columns) != expected_labels:
        raise ValueError(f"The column labels are not as expected. "
                         f"Expected: {expected_labels}, but got: {list(df.columns)}")

    print(f"The column labels are as expected: {list(df.columns)}")

    return None
