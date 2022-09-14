import sys

from BinanceSupervision.resources.Resource_BinanceConnection import Ui_Dialog


from PyQt5.QtWidgets import (
    QDialog
)

class Dialog(QDialog):
    def __init__(self,model,ctrl,signal):
        super().__init__()

        self.model = model
        self.ctrl = ctrl

        self.ui=Ui_Dialog()
        self.ui.setupUi(self)

        key,secret=self.model.getConfig()
        self.setLineEditApiKey(key)
        self.setLineEditApiSecret(secret)

        self.connectSignalSlots()
        self.signal=signal

    def connectSignalSlots(self):
        self.ui.buttonBox.accepted.connect(self.OK)
        self.ui.buttonBox.rejected.connect(self.CANCEL)

    def OK(self):
        self.ctrl.OkClicked(self.getLineEditApiKey(),self.getLineEditApiSecret())
        self.signal.emit()

    def CANCEL(self):
        pass

    def getLineEditApiKey(self):
        return self.ui.lineEdit_apiKey.text()

    def getLineEditApiSecret(self):
        return self.ui.lineEdit_apiSecret.text()

    def setLineEditApiKey(self,key):
        self.ui.lineEdit_apiKey.setText(key)

    def setLineEditApiSecret(self,secret):
        self.ui.lineEdit_apiSecret.setText(secret)
