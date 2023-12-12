from pandas import DataFrame, read_csv

from src.poap.template import tasklist


class ExportManager:

    def __init__(self):
        self.file_name = str()
        self.file_type = str()
        self.location = str()
        self.blank = bool()
        self.sheet_name = int()
        self.meta = str()

    def temp(self):
        pass

    def blank_file(self):
        df = DataFrame(tasklist)
        df.to_csv(r'./data/templates/test1.csv')

