from pandas import DataFrame

from src.poap.templates import tasklist


class Exporter:
    def __int__(self, *args):
        self.args = args


def export_handler(*args):
    print([*args])


def blank_(file_name, file_type, location, meta):
    df_ = DataFrame(tasklist)
    df_.to_excel(r'./test.xlsx')

