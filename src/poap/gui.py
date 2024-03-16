from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QAction
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtGui import QIcon

from src.poap.config import SAMPLE_SVG_PATH, LOGO_PATH
from src.poap.excel import read_excel_file


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

    def select_data(self):
        print("Select Data action triggered")
        dfs = read_excel_file()
        print(dfs['settings'], dfs['timeframes'], dfs['tasks'], sep="\n\n")

    def check_data(self):
        print("Check Data action triggered")

    def download_template(self):
        print("Download Template action triggered")

    def download_svg(self):
        print("Download SVG action triggered")

    def closeEvent(self, event):
        print("Window closed")
        event.accept()
