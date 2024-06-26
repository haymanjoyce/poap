import os

from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QAction, QFileDialog, QDesktopWidget
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from src.poap import LOGO_PATH
from src.poap.template import *
from src.poap.excel import *
from src.poap.checks import *
from src.poap.calcs import *
from src.poap.drawing import *
from src.poap.utils import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Plan on a Page Tool')
        self.setWindowIcon(QIcon(LOGO_PATH))

        # Center window
        self.resize(600, 600)
        screen = QDesktopWidget().screenGeometry()
        window = self.geometry()
        self.move((screen.width() - window.width()) // 2, (screen.height() - window.height()) // 2)

        gui_layout = QVBoxLayout()

        # SVG widget
        # If the SVG content is larger than the widget, it will be scaled down to fit within the widget
        self.svg_widget = QSvgWidget(SAMPLE_SVG_PATH)
        # self.svg_widget.resize(100, 100)
        # self.svg_widget.renderer().setAspectRatioMode(Qt.KeepAspectRatio)
        # self.svg_widget.renderer().setAspectRatioMode(Qt.IgnoreAspectRatio)
        gui_layout.addWidget(self.svg_widget)

        # Draw button
        button = QPushButton("Draw")
        # noinspection PyUnresolvedReferences
        button.clicked.connect(self.draw)
        gui_layout.addWidget(button)

        # Central widget
        central_widget = QWidget()
        central_widget.setLayout(gui_layout)
        self.setCentralWidget(central_widget)

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
            save_excel_file(_dfs, file_name)

    def select_data(self):
        # open dialogue
        last_file_path = get_path('USER_XLSX_PATH')
        last_dir_path = os.path.dirname(last_file_path) if last_file_path else None
        file_name, _filter = QFileDialog.getOpenFileName(self, "Select Spreadsheet", last_dir_path,
                                                         "Excel Files (*.xls *.xlsx)")
        # store path
        if file_name:
            store_path('USER_XLSX_PATH', file_name)

    def check_data(self):
        # get user file path
        file_path = get_path('USER_XLSX_PATH')

        # convert xlsx to dfs
        dfs = return_dfs(file_path)

        # get template values as lists
        _scales = list(scales.keys())

        # check column labels
        check_column_labels(dfs[0], ['key', 'value'])
        check_column_labels(dfs[1], ['key', 'value'])
        check_column_labels(dfs[2], _scales)

    def draw(self):
        # todo save excel and reload
        file_path = get_path('USER_XLSX_PATH')
        dfs = return_dfs(file_path)
        _df = get_df_by_name(dfs, 'frame')
        _df.set_index('key', inplace=True)
        df_dict = _df['value'].to_dict()
        _width = df_dict.get('frame_width')
        _height = df_dict.get('frame_height')
        _units = df_dict.get('frame_units')
        dwg = Drawing()
        dwg.set_view_port(_width, _height, _units)
        dwg.add(dwg.rect((0, 0), (50, 100), fill='red'))
        dwg.add(dwg.text("Hello World", insert=(10, 10)))
        dwg.print_svg()
        dwg.save()
        self.svg_widget.load(SAMPLE_SVG_PATH)

    def download_svg(self):
        print("Download SVG action triggered")

    def closeEvent(self, event):
        print("Window closed")
        event.accept()

