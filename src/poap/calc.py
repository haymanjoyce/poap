import pandas as pd
from typing import AnyStr


def calc_duration(df: pd.DataFrame,
                  start_column: AnyStr, finish_column: AnyStr, duration_column: AnyStr = 'duration') -> pd.DataFrame:
    """
    Calculates the duration between two dates in a DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame to calculate the duration in.
    start_column (AnyStr): The name of the column containing the start dates.
    finish_column (AnyStr): The name of the column containing the finish dates.
    duration_column (AnyStr): The name of the new column to store the duration. Defaults to 'duration'.

    Returns:
    pd.DataFrame: The DataFrame with the new duration column.

    Raises:
    KeyError: If the start_column or finish_column do not exist in the DataFrame.
    """
    if start_column not in df.columns or finish_column not in df.columns:
        raise KeyError(f"Both {start_column} and {finish_column} must exist in the DataFrame")

    df[start_column] = pd.to_datetime(df[start_column])
    df[finish_column] = pd.to_datetime(df[finish_column])

    df[duration_column] = (df[finish_column] - df[start_column]).dt.total_seconds() / 86400

    return df
