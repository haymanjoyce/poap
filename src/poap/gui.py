from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QAction
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtGui import QIcon

from src.poap.config import *
from src.poap.template import *
from src.poap.excel import *
from src.poap.checks import *
from src.poap.calcs import *
from src.poap.svg import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Plan on a Page Tool')
        self.setWindowIcon(QIcon(LOGO_PATH))

        svg_widget = QSvgWidget(SAMPLE_SVG_PATH)
        button = QPushButton("Refresh")
        # noinspection PyUnresolvedReferences
        button.clicked.connect(self.refresh)

        layout = QVBoxLayout()
        layout.addWidget(svg_widget)
        layout.addWidget(button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.resize(600, 600)

        menu_bar = self.menuBar()
        data_menu = menu_bar.addMenu("Data")
        download_menu = menu_bar.addMenu("Download")
        help_menu = menu_bar.addMenu("Help")

        select_data_action = QAction("Select data", self)
        check_data_action = QAction("Check data", self)
        download_template_action = QAction("Download template", self)
        download_svg_action = QAction("Download SVG file", self)

        # noinspection PyUnresolvedReferences
        select_data_action.triggered.connect(self.select_data)
        # noinspection PyUnresolvedReferences
        check_data_action.triggered.connect(self.check_data)
        # noinspection PyUnresolvedReferences
        download_svg_action.triggered.connect(self.download_svg)
        # noinspection PyUnresolvedReferences
        download_template_action.triggered.connect(self.download_template)

        data_menu.addAction(select_data_action)
        data_menu.addAction(check_data_action)
        download_menu.addAction(download_svg_action)
        help_menu.addAction(download_template_action)

    def refresh(self):
        print("Refresh button clicked")
        dfs = read_excel_file()
        dfs['tasks'] = calc_duration(dfs['tasks'])
        page_width = dfs['settings'].loc['page_width', 'value']
        page_height = dfs['settings'].loc['page_height', 'value']
        create_sample_svg(page_width, page_height)

    def select_data(self):
        print("Select Data action triggered")
        dfs = read_excel_file()
        print(dfs['settings'], dfs['timeframes'], dfs['tasks'], sep="\n\n")

    def check_data(self):
        print("Check Data action triggered")
        dfs = read_excel_file()
        check_column_labels(dfs['tasks'], tasks_columns)

    def download_template(self):
        print("Download Template action triggered")
        settings_df = create_settings_df(settings_values, settings_help)
        timeframes_df = create_timeframes_df(timeframes_finish_dates, timeframes_spans)
        tasks_df = create_tasks_df(tasks_tasks, tasks_start_dates, tasks_finish_dates)
        create_excel_file(settings_df, timeframes_df, tasks_df)

    def download_svg(self):
        print("Download SVG action triggered")

    def closeEvent(self, event):
        print("Window closed")
        event.accept()
