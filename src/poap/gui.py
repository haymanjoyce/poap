from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtGui import QIcon

from src.poap.config import SAMPLE_SVG_PATH, LOGO_PATH

from PyQt5.QtWidgets import QMenu, QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Plan on a Page Tool')

        # Set the window icon
        self.setWindowIcon(QIcon(LOGO_PATH))

        # Create a QSvgWidget
        svg_widget = QSvgWidget()
        # Load the SVG image
        svg_widget.load(SAMPLE_SVG_PATH)

        # Create a QPushButton
        button = QPushButton("Refresh")
        # Connect the clicked signal of the button to a function
        button.clicked.connect(self.refresh)

        # Create a QVBoxLayout
        layout = QVBoxLayout()
        # Add the svg_widget and the button to the layout
        layout.addWidget(svg_widget)
        layout.addWidget(button)

        # Create a QWidget and set it as the central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Resize the window
        self.resize(600, 600)

        # Create a menu bar
        menu_bar = self.menuBar()

        # Create a menu
        data_menu = QMenu("Data", self)
        download_menu = QMenu("Download", self)
        help_menu = QMenu("Help", self)

        # Add menus to the menu bar
        menu_bar.addMenu(data_menu)
        menu_bar.addMenu(download_menu)
        menu_bar.addMenu(help_menu)

        # Create actions
        select_data_action = QAction("Select data", self)
        check_data_action = QAction("Check data", self)
        download_template_action = QAction("Download template", self)
        download_svg_action = QAction("Download SVG file", self)

        # Add actions to the menu
        data_menu.addAction(select_data_action)
        data_menu.addAction(check_data_action)
        download_menu.addAction(download_svg_action)
        help_menu.addAction(download_template_action)

        # Connect the triggered signal of the open_action to the open_file function
        select_data_action.triggered.connect(self.select_data)
        check_data_action.triggered.connect(self.check_data)
        download_svg_action.triggered.connect(self.download_svg)
        download_template_action.triggered.connect(self.download_template)

    def refresh(self):
        # This function will be executed when the "Refresh" button is clicked
        print("Refresh button clicked")

    def select_data(self):
        # This function will be executed when the "Select Data" action is triggered
        print("Select Data action triggered")

    def check_data(self):
        # This function will be executed when the "Check Data" action is triggered
        print("Check Data action triggered")

    def download_template(self):
        # This function will be executed when the "Download Template" action is triggered
        print("Download Template action triggered")

    def download_svg(self):
        # This function will be executed when the "Download SVG" action is triggered
        print("Download SVG action triggered")

    def closeEvent(self, event):
        # This function will be executed when the window is closed
        print("Window closed")
        event.accept()
