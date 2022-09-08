import sys

from BinanceSupervision.resources.Resource_main import Ui_MainWindow
from BinanceSupervision.controlers.Ctrl_BinanceConfiguration import Ctrl_BinanceConfiguration
from BinanceSupervision.models.Model_BinanceConfiguration import Model_BinanceConfiguration
from BinanceSupervision.views.View_BinanceConfiguration import Dialog

from PyQt6.QtWidgets import (
    QMainWindow
)

class Window(QMainWindow, Ui_MainWindow):
    Model_BinanceConfig=None
    Ctrl_BinanceConfiguration=None
    View_BinanceConfiguration=None
    def __init__(self, model_app,ctrl_app):
        super().__init__()

        self.model=model_app
        self.ctrl=ctrl_app

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.connectSignalSlots()

    def connectSignalSlots(self):
        self.ui.action_Connect.triggered.connect(self.OpenBinanceConfiguration)
        self.ui.action_Exit.triggered.connect(self.Exit)

    def OpenBinanceConfiguration(self):
        if(self.Model_BinanceConfig==None):
            self.Model_BinanceConfig = Model_BinanceConfiguration()
        if(self.Ctrl_BinanceConfiguration==None):
            self.Ctrl_BinanceConfiguration = Ctrl_BinanceConfiguration(self.Model_BinanceConfig)
        if (self.View_BinanceConfiguration==None):
            self.View_BinanceConfiguration = Dialog(self.Model_BinanceConfig,self.Ctrl_BinanceConfiguration)
        self.View_BinanceConfiguration.exec()

    def Exit(self):
        sys.exit(0)

