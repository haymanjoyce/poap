import pandas as pd


def calc_tasks(df: pd.DataFrame) -> pd.DataFrame:
    df['start'] = pd.to_datetime(df['start'])
    df['finish'] = pd.to_datetime(df['finish'])

    df['duration'] = df['finish'] - df['start']

    df['duration'] = df['duration'].dt.total_seconds() / 86400

    return df
