from src.poap.excel import read_excel_file


def check_timeframes():
    dfs = read_excel_file()
    print(dfs[1])
