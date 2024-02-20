import sys

from src.poap.gui import QApplication, MainWindow, ZoomableSvgWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # svg_widget = ZoomableSvgWidget()
    # svg_widget.show()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


