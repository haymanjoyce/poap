import sys

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtSvg import QSvgWidget


class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Python Menus & Toolbars")
        # self.resize(400, 200)
        # self.centralWidget = QLabel("Hello, World")
        # self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # self.setCentralWidget(self.centralWidget)
        self.create_svg()

    def create_svg(self):
        svg = QSvgWidget('../../data/svgs/gaussian1.svg', parent=self)
        svg.setGeometry(QRect(0, 0, 800, 600))
        self.resize(svg.width(), svg.height())
        svg.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

