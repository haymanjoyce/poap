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


def return_excel_file(dfs: List[pd.DataFrame], sheet_names: List[str], file_path: str = SAMPLE_XLSX_PATH) -> None:
    with pd.ExcelWriter(file_path) as writer:
        for df, sheet_name in zip(dfs, sheet_names):
            df.to_excel(writer, sheet_name=sheet_name)


def return_dfs(excel_file: Optional[str] = SAMPLE_XLSX_PATH) -> List[pd.DataFrame]:
    xls = pd.ExcelFile(excel_file)
    _sheet_names = xls.sheet_names
    dfs = [xls.parse(sheet_name) for sheet_name in _sheet_names]
    return dfs


# todo ensure df variable name same as sheet name

from src.poap.template import *
# scales = return_df_col_labels(scales)
# return_excel_file([scales,], '../../data/excel/sample.xlsx')
# dfs = return_dfs('../../data/excel/sample.xlsx')
# print(dfs)

