import sys

from src.poap.gui import QApplication, MainWindow

from df import create_excel_file, read_excel_file


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # window = MainWindow()
    # window.show()
    # sys.exit(app.exec_())
    dfs = read_excel_file()
    date = dfs[1].loc[0, 'start']
    print(type(date))
