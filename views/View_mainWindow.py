import os,sys,logging

from BinanceSupervision.controlers.Ctrl_BinanceClient import Ctrl_BinanceClient
from BinanceSupervision.models.Model_BinanceClient import Model_BinanceClient
from BinanceSupervision.resources.Resource_main import Ui_MainWindow
from BinanceSupervision.controlers.Ctrl_BinanceConfiguration import Ctrl_BinanceConfiguration
from BinanceSupervision.models.Model_BinanceConfiguration import Model_BinanceConfiguration
from BinanceSupervision.views.View_BinanceConfiguration import Dialog
from PyQt5 import QtCore

from PyQt5.QtWidgets import (
    QMainWindow
)

FORMAT = '%(asctime)s %(username)s:     %(message)s'
logging.basicConfig(handlers=[logging.FileHandler(filename="system.log",
                                                 encoding='utf-8', mode='a+')],
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%F %A %T",
                    level=logging.INFO)


class Window(QMainWindow, Ui_MainWindow):
    SignalConfigSet=QtCore.pyqtSignal()
    Model_BinanceConfiguration=None
    Ctrl_BinanceClient=None
    Ctrl_BinanceConfiguration=None
    View_BinanceConfiguration=None
    def __init__(self, model_app,ctrl_app):
        super().__init__()

        self.model=model_app
        self.ctrl=ctrl_app

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.connectSignalSlots()

        logging.info("Starting")

    def connectSignalSlots(self):
        self.ui.action_Connect.triggered.connect(self.OpenBinanceConfiguration)
        self.ui.action_Exit.triggered.connect(self.Exit)
        self.SignalConfigSet.connect(self.BinanceConfigured)

    def OpenBinanceConfiguration(self):
        if(self.Model_BinanceConfiguration==None):
            self.Model_BinanceConfiguration = Model_BinanceConfiguration()
        if(self.Ctrl_BinanceConfiguration==None):
            self.Ctrl_BinanceConfiguration = Ctrl_BinanceConfiguration(self.Model_BinanceConfiguration)
        if (self.View_BinanceConfiguration==None):
            self.View_BinanceConfiguration = Dialog(self.Model_BinanceConfiguration,self.Ctrl_BinanceConfiguration,self.SignalConfigSet)

        self.View_BinanceConfiguration.exec()

    def Exit(self):
        if (self.Ctrl_BinanceClient != None):
            self.Ctrl_BinanceClient.disconnect()
        logging.info("Bye-bye")
        sys.exit(0)

    def BinanceConfigured(self):
        if (self.Ctrl_BinanceClient == None):
            self.Ctrl_BinanceClient=Ctrl_BinanceClient(Model_BinanceClient(self.Model_BinanceConfiguration))
        else:
            self.Ctrl_BinanceClient.updateConfig(self.Model_BinanceConfiguration)



