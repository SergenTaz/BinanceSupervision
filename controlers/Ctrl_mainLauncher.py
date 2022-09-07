import sys

from PyQt6.QtWidgets import (
    QApplication
)
from BinanceSupervision.views.View_mainWindow import Window
from BinanceSupervision.controlers.Ctrl_BinanceConnection import Ctrl_BinanceConnection

class mainLauncher():
    win = None
    def __init__(self, parent=None):
        app = QApplication(sys.argv)
        self.win = Window()
        self.connectSignalSlots()
        self.win.show()
        sys.exit(app.exec())

    def connectSignalSlots(self):
        self.win.action_Connect.triggered.connect(self.openConnectionDialog)
        self.win.action_Exit.triggered.connect(self.close)
        
    def openConnectionDialog(self):
        Ctrl_BinanceConnection(self.win)
    def close(self):
        sys.exit(0)