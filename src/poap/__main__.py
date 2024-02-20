import sys
import pathlib

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtSvg import QSvgWidget


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSvgWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SVG Main Window')

        # Create a QSvgWidget
        svg_widget = QSvgWidget()

        # Set the size of the QSvgWidget
        svg_widget.setGeometry(100, 100, 400, 400)

        # Load the SVG image
        svg_widget.load('image.svg')

        # Set the central widget
        self.setCentralWidget(svg_widget)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



