from pandas import read_csv
from pathlib import Path
from time import ctime

from pathvalidate import *

from src.poap.utils import get_config_dict


class ExportManager:

    def __init__(self, file_name, file_type, location, blank, sheet_name, meta):
        self.file_name = self.set_file_name(file_name)
        self.file_type = file_type
        self.file_path = location
        self.blank = blank
        self.sheet_name = sheet_name
        self.meta = meta

    def set_file_name(self, file_name):
        if not file_name:
            saved_name = get_config_dict().__getitem__("export_path").__getitem__("name")
            if not saved_name:
                return f'export_{ctime().replace(" ", "_")}'
            else:
                return saved_name
        else:
            pass

    def set_file_type(self):
        pass

    def set_location(self):
        if not self.file_path:
            self.file_path = Path.home()

    def set_sheet_name(self):
        pass

    def set_meta(self):
        pass

    def export_csv(self):
        try:
            df = read_csv(r'./data/templates/tasks.csv')
            df.to_csv(r'./data/templates/test4.csv')
        except FileNotFoundError:
            print('Template file not found.')

    def export_xlsx(self):
        pass

    def export_json(self):
        pass

    def export_svg(self):
        pass

    def export_pdf(self):
        pass

    def export_png(self):
        pass

    def export_pkl(self):
        pass

