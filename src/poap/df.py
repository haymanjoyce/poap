from typing import List
import pandas as pd

from config import SAMPLE_XLSX_PATH


def create_settings_df() -> pd.DataFrame:
    settings_quantity: int = 3

    blank_list: List[str] = ['' for _ in range(settings_quantity)]

    settings_cols: dict = {
        'value': blank_list,
        'help': blank_list,
    }

    settings_labels: List[str] = ['height', 'width', 'rows']

    settings_df: pd.DataFrame = pd.DataFrame(settings_cols, index=settings_labels)

    settings_df.loc['height'] = [100, 'The height of the object']
    settings_df.loc['width'] = [200, 'The width of the object']
    settings_df.loc['rows'] = [5, 'The number of rows in the object']

    return settings_df


def create_tasks_df() -> pd.DataFrame:
    tasks_cols: dict = {
        'task': ['task1', 'task2', 'task3'],
        'start': ['', '', ''],
        'finish': ['', '', ''],
    }

    tasks_df: pd.DataFrame = pd.DataFrame(tasks_cols)

    return tasks_df


def create_excel_file(file_path: str = SAMPLE_XLSX_PATH) -> None:
    settings_df: pd.DataFrame = create_settings_df()
    tasks_df: pd.DataFrame = create_tasks_df()

    with pd.ExcelWriter(f'{file_path}') as writer:
        settings_df.to_excel(writer, sheet_name='settings')
        tasks_df.to_excel(writer, sheet_name='tasks')


def read_excel_file(file_path: str = SAMPLE_XLSX_PATH) -> List[pd.DataFrame]:
    dfs: List[pd.DataFrame] = [pd.read_excel(file_path, sheet_name=sheet) for sheet in ['settings', 'tasks']]
    return dfs
