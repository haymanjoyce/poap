import sys

from src.poap.gui import QApplication, MainWindow

import src.poap.df

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # window = MainWindow()
    # window.show()
    sys.exit(app.exec_())
