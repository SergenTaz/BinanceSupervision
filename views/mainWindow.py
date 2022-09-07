from BinanceSupervision.models.untitled import Ui_MainWindow

from PyQt6.QtWidgets import (

    QMainWindow

)

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)