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
        if file_name:
                clean_name = 'clean_name'
                # save clean_name
                return clean_name
        else:
            saved_name = get_config_dict().__getitem__("export_path").__getitem__("name")
        if saved_name:
            # check it doesn't exist (for extension) at location
            return saved_name
        else:
            modified_name = 'modified_name'
            # check name with filetype doesn't already exist at location and edit if it does
            # keep checking until no such edited name at location
            # save it if edited

            auto_name = f'export_{ctime().replace(" ", "_")}'
            return modified_name

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

