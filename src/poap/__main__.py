"""
This module, `src/poap/__main__.py`, serves as the main entry point for the application. 

It imports necessary modules and functions from PyQt5 and the custom `MainWindow` class from `src.poap.gui`. 

The application is initiated here with the creation of an instance of QApplication and MainWindow.

The main window is then displayed and the application's event loop is started.

This module is executed when you run the script directly, not when imported as a module.

Functions:
    None

Classes:
    None

Exceptions:
    None

"""
import sys
from PyQt5.QtWidgets import QApplication
from src.poap.gui import MainWindow

# This is the main entry point of the application.
if __name__ == '__main__':
    # Create an instance of QApplication
    app = QApplication(sys.argv)

    # Create an instance of MainWindow, which is the main window of the application
    window = MainWindow()

    # Show the main window
    window.show()

    # Start the application's event loop
    sys.exit(app.exec_())
