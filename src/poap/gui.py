import os
import pathlib

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QGraphicsView, QVBoxLayout, QWidget
from PyQt5.QtSvg import QSvgWidget, QGraphicsSvgItem

import utils


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SVG Main Window')

        # Create a QSvgWidget
        svg_widget = QSvgWidget()

        # Set the size of the QSvgWidget
        # svg_widget.setGeometry(100, 100, 400, 400)

        # Load the SVG image
        svg_file = utils.get_abs_path()
        svg_widget.load(svg_file.__str__())

        # Set the central widget
        self.setCentralWidget(svg_widget)


class ZoomableSvgWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.svg_item = QGraphicsSvgItem(utils.get_abs_path())
        self.graphics_view = QGraphicsView(self)
        self.graphics_view.setScene(self.svg_item.scene())
        layout = QVBoxLayout()
        layout.addWidget(self.graphics_view)
        self.setLayout(layout)

    def wheelEvent(self, event):
        factor = 1.1 if event.angleDelta().y() > 0 else 0.9
        self.graphics_view.scale(factor, factor)
        event.accept()
