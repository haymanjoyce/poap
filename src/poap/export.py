from pandas import read_csv
from pathlib import Path
from time import ctime


class ExportManager:

    def __init__(self, file_name, file_type, location, blank, sheet_name, meta):
        self.file_name = file_name
        self.file_type = file_type
        self.location = location
        self.blank = blank
        self.sheet_name = sheet_name
        self.meta = meta

    def manage(self):
        self.defaults()

    def defaults(self):
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

