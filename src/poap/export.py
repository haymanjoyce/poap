from pandas import DataFrame

from src.poap.templates import tasklist


def blank_(path_):
    df_ = DataFrame(tasklist)
    if path_:
        df_.to_excel(path_)
    else:
        df_.to_excel(r'./test.xlsx')

# build and export template xls

