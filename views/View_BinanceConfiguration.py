import sys

from BinanceSupervision.resources.Resource_BinanceConnection import Ui_Dialog


from PyQt6.QtWidgets import (
    QDialog
)

class Dialog(QDialog):
    def __init__(self,model,ctrl):
        super().__init__()

        self.model = model
        self.ctrl = ctrl

        self.ui=Ui_Dialog()
        self.ui.setupUi(self)

        self.connectSignalSlots()

    def connectSignalSlots(self):
        self.ui.buttonBox.accepted.connect(self.OK)
        self.ui.buttonBox.rejected.connect(self.CANCEL)

    def OK(self):
        self.ctrl.OkClicked(self.getLineEditApiKey(),self.getLineEditApiSecret())

    def CANCEL(self):
        pass

    def getLineEditApiKey(self):
        return self.ui.lineEdit_apiKey.text()

    def getLineEditApiSecret(self):
        return self.ui.lineEdit_apiSecret.text()
