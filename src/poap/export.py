from pandas import read_csv
from pathlib import Path
from time import ctime


class ExportManager:

    def __init__(self):
        self.file_name = str()
        self.file_type = str()
        self.location = str()
        self.blank = str()
        self.sheet_name = int()
        self.meta = str()

    def execute(self):
        self.set_defaults()

    def set_defaults(self):
        if not self.location:
            self.location = Path.home()
        if not self.file_name:
            self.file_name = f'export_{ctime().replace(" ", "_")}'

    def blank_file(self):
        try:
            df = read_csv(r'./data/templates/tasks.csv')
            df.to_csv(r'./data/templates/test4.csv')
        except FileNotFoundError:
            print('Template file not found.')

