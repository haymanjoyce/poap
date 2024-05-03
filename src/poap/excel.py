import os
import shutil
from typing import Dict, List, Optional
import pandas as pd

from src.poap import SAMPLE_XLSX_PATH, TEMP_XLSX_PATH


def return_df_row_labels(data: Dict, name: str) -> pd.DataFrame:
    keys = data.keys()
    values = data.values()
    _df = pd.DataFrame(columns=['key', 'value'])
    _df['key'] = list(keys)
    _df['value'] = list(values)
    _df.name = name
    return _df


def return_df_col_labels(data: Dict, name: str) -> pd.DataFrame:
    _df = pd.DataFrame(data)
    _df.name = name
    return _df


def save_excel_file(_dfs: List[pd.DataFrame], file_path: str = SAMPLE_XLSX_PATH) -> None:
    with pd.ExcelWriter(file_path) as writer:
        for _df in _dfs:
            _df.to_excel(writer, sheet_name=_df.name, index=False)


def return_dfs(excel_file: Optional[str] = SAMPLE_XLSX_PATH) -> List[pd.DataFrame]:
    # Pandas reads and closes the file
    # If file open in Excel, Excel will not be able to save changes after pandas operation
    # And so we copy the file to a temp location and read that file
    shutil.copy2(excel_file, TEMP_XLSX_PATH)
    xls = pd.ExcelFile(TEMP_XLSX_PATH)
    _dfs = [xls.parse(sheet_name) for sheet_name in xls.sheet_names]
    for i, _df in enumerate(_dfs):
        _df.name = xls.sheet_names[i]
    return _dfs

