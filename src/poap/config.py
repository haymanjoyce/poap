SAMPLE_XLSX_PATH = 'data/excel/sample.xlsx'
SAMPLE_SVG_PATH = 'data/svg/sample.svg'
SAMPLE_SVG_SCALED_PATH = 'data/svg/sample_scaled.svg'
LOGO_PATH = 'data/images/logo.ico'
USER_XLSX_PATH = None


def set_user_xlsx_path(path: str):
    global USER_XLSX_PATH
    USER_XLSX_PATH = path
    return USER_XLSX_PATH
