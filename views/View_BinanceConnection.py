from BinanceSupervision.models.Model_BinanceConnection import Ui_Dialog

from PyQt6.QtWidgets import (
    QDialog
)

class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
#        self.setupUi(self)
