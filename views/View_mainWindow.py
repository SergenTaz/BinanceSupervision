import os,sys,logging

from BinanceSupervision.controlers.Ctrl_BinanceClient import Ctrl_BinanceClient
from BinanceSupervision.models.Model_BinanceClient import Model_BinanceClient
from BinanceSupervision.resources.Resource_main import Ui_MainWindow
from BinanceSupervision.controlers.Ctrl_BinanceConfiguration import Ctrl_BinanceConfiguration
from BinanceSupervision.models.Model_BinanceConfiguration import Model_BinanceConfiguration
from BinanceSupervision.views.View_BinanceConfiguration import Dialog
from PyQt6 import QtCore

from PyQt6.QtWidgets import (
    QMainWindow
)

FORMAT = '%(asctime)s %(username)s:     %(message)s'
logging.basicConfig(format=FORMAT, datefmt='%m/%d/%Y %I:%M:%S %p',filename='system.log', encoding='utf-8', level=logging.DEBUG)
d = {'username': os.getlogin()}

class Window(QMainWindow, Ui_MainWindow):
    SignalConfigSet=QtCore.pyqtSignal()
    Model_BinanceConfiguration=None
    Model_BinanceClient=None
    Ctrl_BinanceConfiguration=None
    View_BinanceConfiguration=None
    def __init__(self, model_app,ctrl_app):
        super().__init__()

        self.model=model_app
        self.ctrl=ctrl_app

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.connectSignalSlots()

        logging.info("Starting", extra=d)

    def connectSignalSlots(self):
        self.ui.action_Connect.triggered.connect(self.OpenBinanceConfiguration)
        self.ui.action_Exit.triggered.connect(self.Exit)

    def OpenBinanceConfiguration(self):
        if(self.Model_BinanceConfiguration==None):
            self.Model_BinanceConfiguration = Model_BinanceConfiguration()
        if(self.Ctrl_BinanceConfiguration==None):
            self.Ctrl_BinanceConfiguration = Ctrl_BinanceConfiguration(self.Model_BinanceConfiguration)
        if (self.View_BinanceConfiguration==None):
            self.View_BinanceConfiguration = Dialog(self.Model_BinanceConfiguration,self.Ctrl_BinanceConfiguration,self.SignalConfigSet)
        self.SignalConfigSet.connect(self.BinanceConfigured)
        self.View_BinanceConfiguration.exec()

    def Exit(self):
        logging.info("Bye-bye", extra=d)
        sys.exit(0)

    def BinanceConfigured(self):
        if (self.Model_BinanceClient == None):
            self.Model_BinanceClient=Model_BinanceClient(self.Model_BinanceConfiguration)
            self.Ctrl_BinanceClient=Ctrl_BinanceClient(self.Model_BinanceClient)
        else:
            self.Ctrl_BinanceClient.updateConfig(self.Model_BinanceConfiguration)



