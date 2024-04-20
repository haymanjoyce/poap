from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QAction, QFileDialog
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from src.poap.config import *
from src.poap.template import *
from src.poap.excel import *
from src.poap.checks import *
from src.poap.calcs import *
from src.poap.svg import *
from src.poap.utils import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Plan on a Page Tool')
        self.setWindowIcon(QIcon(LOGO_PATH))

        self.svg_widget = QSvgWidget(SAMPLE_SVG_PATH)
        self.svg_widget.renderer().setAspectRatioMode(Qt.KeepAspectRatio)
        button = QPushButton("Refresh")
        # noinspection PyUnresolvedReferences
        button.clicked.connect(self.refresh)

        gui_layout = QVBoxLayout()
        gui_layout.addWidget(self.svg_widget)
        gui_layout.addWidget(button)

        central_widget = QWidget()
        central_widget.setLayout(gui_layout)
        self.setCentralWidget(central_widget)
        self.resize(100, 100)

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

    def download_template(self):
        # create dfs
        _frame = return_df_row_labels(frame, 'frame')
        _layout = return_df_row_labels(layout, 'layout')
        _scales = return_df_col_labels(scales, 'scales')
        _dfs = [_frame, _layout, _scales]

        # open dialogue
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _filter = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                         "Excel Files (*.xls *.xlsx)", options=options)
        # save file
        if file_name:
            print(f'File path: {file_name, _filter}')
            save_excel_file(_dfs, file_name)

    def select_data(self):
        print("Select Data action triggered")
        file_name, _filter = QFileDialog.getOpenFileName(self, "Select Spreadsheet", "",
                                                         "Excel Files (*.xls *.xlsx)")
        if file_name:
            print(f'File path: {file_name, _filter}')
            USER_XLSX_PATH = file_name
            set_user_xlsx_path(file_name)
            print(USER_XLSX_PATH)

            store_path('USER_XLSX_PATH', file_name)
            print(USER_XLSX_PATH)

# todo replace config py with config.json then import json vars at package init

    def check_data(self):
        print("Check Data action triggered")
        dfs = return_dfs()
        df = [df for df in dfs if df.name == 'scales'][0]
        print(df.name)
        # dfs = return_dfs(file_name)
        # check column labels
        check_column_labels(dfs[0], ['key', 'value'])
        check_column_labels(dfs[1], ['key', 'value'])
        check_column_labels(dfs[2], ['key', 'value'])

    def download_svg(self):
        print("Download SVG action triggered")

    def refresh(self):
        print("Refresh button clicked")
        dwg = Drawing(return_dfs())
        dwg.set_view_port(200, 200)
        dwg.add_frame()
        dwg.save_drawing()
        self.update()

    def closeEvent(self, event):
        print("Window closed")
        event.accept()
