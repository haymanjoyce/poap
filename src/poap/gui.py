from PyQt5.QtWidgets import QMainWindow
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

        # Set the central widget
        self.setCentralWidget(svg_widget)

        # Create a menu bar
        menu_bar = self.menuBar()

        # Create a menu
        file_menu = QMenu("File", self)
        menu_bar.addMenu(file_menu)

        # Create actions
        open_action = QAction("Open", self)
        download_template_action = QAction("Download Template", self)

        # Connect the triggered signal of the open_action to the open_file function
        open_action.triggered.connect(self.open_file)  # noinspection PyUnresolvedReferences

        # Add actions to the menu
        file_menu.addAction(open_action)
        file_menu.addAction(download_template_action)

        # Resize the window
        self.resize(600, 600)

    def open_file(self):
        # This function will be executed when the "Open" action is triggered
        print("Open action triggered")
