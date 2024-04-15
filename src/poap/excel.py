"""
excel.py

This module provides functions to create and read Excel files from pandas DataFrames.
"""

from typing import Dict, List, Optional
import pandas as pd

from src.poap.config import SAMPLE_XLSX_PATH


def return_df_row_labels(data: Dict, name: str) -> pd.DataFrame:
    keys = data.keys()
    values = data.values()
    df = pd.DataFrame(columns=['key', 'value'])
    df['key'] = list(keys)
    df['value'] = list(values)
    df.name = name
    return df


def return_df_col_labels(data: Dict, name: str) -> pd.DataFrame:
    df = pd.DataFrame(data)
    df.name = name
    return df


def save_excel_file(_dfs: List[pd.DataFrame], file_path: str = SAMPLE_XLSX_PATH) -> None:
    with pd.ExcelWriter(file_path) as writer:
        for df in _dfs:
            df.to_excel(writer, sheet_name=df.name)


def return_dfs(excel_file: Optional[str] = SAMPLE_XLSX_PATH) -> List[pd.DataFrame]:
    xls = pd.ExcelFile(excel_file)
    _dfs = [xls.parse(sheet_name) for sheet_name in xls.sheet_names]
    for i, _df in enumerate(_dfs):
        _df.name = xls.sheet_names[i]
    return _dfs


# from src.poap.template import *
# scales = return_df_col_labels(scales, 'scales')
# save_excel_file([scales, ], '../../data/excel/sample.xlsx')
# dfs = return_dfs('../../data/excel/sample.xlsx')
# df = dfs[0]
# print(df.name)
