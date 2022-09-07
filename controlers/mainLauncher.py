import sys

from PyQt6.QtWidgets import (

    QApplication

)
from BinanceSupervision.views.mainWindow import Window

class mainLaucnher():
    def __init__(self, parent=None):
        app = QApplication(sys.argv)
        win = Window()
        win.show()
        sys.exit(app.exec())