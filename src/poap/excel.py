"""
excel.py

This module provides functions to create and read Excel files from pandas DataFrames.
"""

from typing import Dict, List, Optional
import pandas as pd

from src.poap.config import SAMPLE_XLSX_PATH


def create_settings_df(settings_values: Dict[str, str], settings_help: Dict[str, str]) -> pd.DataFrame:
    """
    Creates a DataFrame from the provided settings values and help texts.

    Parameters:
    settings_values (Dict[str, str]): A dictionary where the keys are the setting labels and the values
    are the setting values.
    settings_help (Dict[str, str]): A dictionary where the keys are the setting labels and the values
    are the help texts for the settings.

    Returns:
    pd.DataFrame: A DataFrame with the setting values and help texts.

    Raises:
    TypeError: If either settings_values or settings_help is not a dictionary.
    """
    if not isinstance(settings_values, dict) or not isinstance(settings_help, dict):
        raise TypeError("Both 'settings_values' and 'settings_help' must be dictionaries")

    try:
        settings_cols: dict = {
            'value': list(settings_values.values()),
            'help': list(settings_help.values()),
        }

        settings_labels: List[str] = list(settings_values.keys())

        settings_df: pd.DataFrame = pd.DataFrame(settings_cols, index=settings_labels)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return pd.DataFrame()

    return settings_df


def create_timeframes_df(finish_dates: List[str], spans: List[float]) -> pd.DataFrame:
    """
    Creates a DataFrame from the provided finish dates and spans.

    Parameters:
    finish_dates (List[str]): A list of finish dates.
    spans (List[float]): A list of spans.

    Returns:
    pd.DataFrame: A DataFrame with the finish dates and spans.

    Raises:
    TypeError: If either finish_dates or spans is not a list.
    """
    if not isinstance(finish_dates, list) or not isinstance(spans, list):
        raise TypeError("Both 'finish_dates' and 'spans' must be lists")

    try:
        timeframes_cols: dict = {
            'finish': finish_dates,
            'span': spans,
        }

        timeframes_df: pd.DataFrame = pd.DataFrame(timeframes_cols)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return pd.DataFrame()

    return timeframes_df


def create_tasks_df(tasks: List[str], start_dates: List[str], finish_dates: List[str]) -> pd.DataFrame:
    """
    Creates a DataFrame from the provided tasks, start dates, and finish dates.

    Parameters:
    tasks (List[str]): A list of tasks.
    start_dates (List[str]): A list of start dates.
    finish_dates (List[str]): A list of finish dates.

    Returns:
    pd.DataFrame: A DataFrame with the tasks, start dates, and finish dates.

    Raises:
    TypeError: If either tasks, start_dates, or finish_dates is not a list.
    """
    if not isinstance(tasks, list) or not isinstance(start_dates, list) or not isinstance(finish_dates, list):
        raise TypeError("'tasks', 'start_dates', and 'finish_dates' must be lists")

    try:
        tasks_cols: dict = {
            'task': tasks,
            'start': start_dates,
            'finish': finish_dates,
        }

        tasks_df: pd.DataFrame = pd.DataFrame(tasks_cols)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return pd.DataFrame()

    return tasks_df


def create_excel_file(settings_df: Optional[pd.DataFrame] = None, timeframes_df: Optional[pd.DataFrame] = None,
                      tasks_df: Optional[pd.DataFrame] = None, file_path: str = SAMPLE_XLSX_PATH) -> None:
    """
    Creates an Excel file from the provided dataframes.

    Parameters:
    settings_df (pd.DataFrame, optional): A DataFrame with the settings. Defaults to None.
    timeframes_df (pd.DataFrame, optional): A DataFrame with the timeframes. Defaults to None.
    tasks_df (pd.DataFrame, optional): A DataFrame with the tasks. Defaults to None.
    file_path (str, optional): The path to the file where the Excel file will be created. Defaults to SAMPLE_XLSX_PATH.

    Raises:
    TypeError: If file_path is not a string.
    """
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")

    try:
        with pd.ExcelWriter(f'{file_path}') as writer:
            if settings_df is not None:
                settings_df.to_excel(writer, sheet_name='settings')
            if timeframes_df is not None:
                timeframes_df.to_excel(writer, sheet_name='timeframes')
            if tasks_df is not None:
                tasks_df.to_excel(writer, sheet_name='tasks')

    except FileNotFoundError:
        print("The file does not exist")

    except PermissionError:
        print("You do not have the necessary permissions to access the file")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None


def read_excel_file(file_path: str = SAMPLE_XLSX_PATH) -> Dict[str, pd.DataFrame]:
    """
    Reads an Excel file and returns a dictionary of pandas DataFrames.

    Parameters:
    file_path (str): The path to the Excel file. Defaults to SAMPLE_XLSX_PATH.

    Returns:
    Dict[str, pd.DataFrame]: A dictionary where the keys are the sheet names
    and the values are the corresponding DataFrames.

    Raises:
    TypeError: If file_path is not a string.
    FileNotFoundError: If the file does not exist.
    PermissionError: If the necessary permissions to access the file are not available.
    Exception: If an unexpected error occurred.
    """
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")

    try:
        xls = pd.ExcelFile(file_path)
    except FileNotFoundError:
        raise FileNotFoundError("The file does not exist")
    except PermissionError:
        raise PermissionError("You do not have the necessary permissions to access the file")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")

    sheet_names = xls.sheet_names
    dfs = {}

    for sheet in sheet_names:
        try:
            df = pd.read_excel(file_path, sheet_name=sheet, index_col=0)
            df.name = sheet
            dfs[sheet] = df
        except Exception as e:
            raise Exception(f"An unexpected error occurred while reading the sheet {sheet}: {e}")

    return dfs
