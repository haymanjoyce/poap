"""
excel.py

This module provides functions to create and read Excel files from pandas DataFrames.
"""

from typing import Dict, List, Optional
import pandas as pd

from src.poap.config import SAMPLE_XLSX_PATH


def return_df_row_labels(data: Dict) -> pd.DataFrame:
    keys = data.keys()
    values = data.values()
    df = pd.DataFrame(columns=['key', 'value'])
    df['key'] = list(keys)
    df['value'] = list(values)
    print(df)
    return df


def return_df_col_labels(data: Dict) -> pd.DataFrame:
    df = pd.DataFrame(data)
    print(df)
    return df


def return_excel_file(dfs: List, file_path: str = SAMPLE_XLSX_PATH) -> None:
    pass


def return_dfs(excel_file: Optional[str] = None) -> List:
    pass


from src.poap.template import *

return_df_col_labels(scales)

