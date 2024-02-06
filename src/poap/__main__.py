import sys
import pathlib

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
        rel_path = 'data/svgs/gaussian_blur.svg'.strip()
        cwd = pathlib.Path.cwd()
        path = pathlib.Path.joinpath(cwd, rel_path)
        # path = pathlib.Path('data/svgs/gaussian_blur.svg').absolute()
        print(path)
        print(path.is_file())
        svg = QSvgWidget(str(path), parent=self)
        svg.setGeometry(QRect(0, 0, 600, 600))
        self.resize(svg.width(), svg.height())
        svg.show()


def test():
    cwd = pathlib.Path.cwd()
    print(cwd)
    file = pathlib.Path('data/svgs/gaussian_blur.svg').absolute()
    print(file)
    print(file.is_file())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

