import csv
import pandas as pd
from typing import List, Tuple, Dict


class Temp:
    def __int__(self, file_name):
        self.file_name = file_name


def read_file_csv(file_name: str) -> pd.DataFrame:
    df = pd.read_csv(file_name)
    print(df.to_string())
    return df


def read_file_xls(filename: str) -> pd.DataFrame:
    pass


def read_file_json(file_name: str) -> pd.DataFrame:
    pass


def merge_file_csv():
    pass


def merge_file_xls():
    pass


def merge_file_json():
    pass


def save_file_csv(file_name: str) -> None:
    pass


def save_file_xls(file_name: str) -> None:
    pass


def save_file_json(file_name: str) -> None:
    pass

