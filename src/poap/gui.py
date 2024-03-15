import os
import pathlib

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QGraphicsView, QVBoxLayout, QWidget
from PyQt5.QtSvg import QSvgWidget, QGraphicsSvgItem

from src.poap.config import SAMPLE_SVG_PATH


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SVG Main Window')

        # Create a QSvgWidget
        svg_widget = QSvgWidget()

        # Set the size of the QSvgWidget
        # svg_widget.setGeometry(100, 100, 400, 400)

        # Load the SVG image
        svg_file = SAMPLE_SVG_PATH
        svg_widget.load(svg_file.__str__())

        # Set the central widget
        self.setCentralWidget(svg_widget)
