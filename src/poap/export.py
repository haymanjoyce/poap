from pandas import DataFrame

from src.poap.templates import tasklist


def blank_(file_name, file_type, location, meta):
    df_ = DataFrame(tasklist)
    df_.to_excel(r'./test.xlsx')

