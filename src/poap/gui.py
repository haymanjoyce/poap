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

        # Create an action
        open_action = QAction("Open", self)
        file_menu.addAction(open_action)

        self.resize(600, 600)
