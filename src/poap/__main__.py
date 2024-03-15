import sys

from src.poap.gui import QApplication, MainWindow

from src.poap.template import *
from src.poap.excel import *
from src.poap.check import *
from src.poap.calc import *
from src.poap.parse import *


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # window = MainWindow()
    # window.show()
    # sys.exit(app.exec_())
    # create_excel_file()

    # settings_df = create_settings_df(settings_values, settings_help)
    # timeframes_df = create_timeframes_df(timeframes_finish_dates, timeframes_spans)
    # tasks_df = create_tasks_df(tasks_tasks, tasks_start_dates, tasks_finish_dates)
    # create_excel_file(settings_df, timeframes_df, tasks_df)

    dfs = read_excel_file()

    # check_column_labels(dfs['tasks'], tasks_columns)
    # dfs['tasks'] = calc_duration(dfs['tasks'], 'start', 'finish')

    print(dfs['settings'])
    print("\n")
    print(dfs['tasks'])

    create_sample_svg()
