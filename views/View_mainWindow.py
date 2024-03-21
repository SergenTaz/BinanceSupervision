import os,sys,logging

from PyQt5.QtCore import QFile
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore

from PyQt5.QtWidgets import (
    QMainWindow, QFileDialog
)

from controlers.Ctrl_BinanceClient import Ctrl_BinanceClient
from controlers.Ctrl_History import Ctrl_History
from controlers.Ctrl_BinanceConfiguration import Ctrl_BinanceConfiguration
from controlers.Ctrl_FileParser import Ctrl_FileParser

from models.Model_BinanceClient import Model_BinanceClient
from models.Model_BinanceReportAnalyze import Model_BinanceReportAnalyze
from models.Model_BinanceConfiguration import Model_BinanceConfiguration

from resources.Resource_main import Ui_MainWindow
from views.View_BinanceConfiguration import Dialog

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
    history=None
    def __init__(self, model_app,ctrl_app):
        super().__init__()

        self.model=model_app
        self.ctrl=ctrl_app

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.connectSignalSlots()

        logging.info("Starting")

    def connectSignalSlots(self):
        self.ui.action_Connect.triggered.connect(self.openBinanceConfiguration)
        self.ui.action_Disconnect.triggered.connect(self.disconnectBinance)
        self.ui.action_Exit.triggered.connect(self.exit)
        self.SignalConfigSet.connect(self.binanceConfigured)
        self.ui.btn_LoadFile.clicked.connect(self.loadFile)
        self.ui.btn_parseFile.clicked.connect(self.parseFile)
        self.ui.btn_AnalyzeFile.clicked.connect(self.analyzeFile)

    def openBinanceConfiguration(self):
        if self.Model_BinanceConfiguration is None:
            self.Model_BinanceConfiguration = Model_BinanceConfiguration()
        if self.Ctrl_BinanceConfiguration is None:
            self.Ctrl_BinanceConfiguration = Ctrl_BinanceConfiguration(self.Model_BinanceConfiguration)
        if self.View_BinanceConfiguration is None:
            self.View_BinanceConfiguration = Dialog(self.Model_BinanceConfiguration,self.Ctrl_BinanceConfiguration,self.SignalConfigSet)

        self.View_BinanceConfiguration.exec()

    def exit(self):
        if self.Ctrl_BinanceClient is not None:
            self.Ctrl_BinanceClient.disconnect()
        sys.exit(0)

    def binanceConfigured(self):
        if self.Ctrl_BinanceClient is None:
            self.Ctrl_BinanceClient=Ctrl_BinanceClient(Model_BinanceClient(self.Model_BinanceConfiguration))
        else:
            self.Ctrl_BinanceClient.updateConfig(self.Model_BinanceConfiguration)
        self.ui.label_BinanceState.setText("Binance connected")

    def loadFile(self):
        file=QFileDialog.getOpenFileName(self, "Open File", "","CSV File (*.csv);;Excel File (*.xlsx);;All Files (*)")
        if file:
            self.ui.le_PathFile.setText(str(file[0]))

    def parseFile(self):
        pass
        # filePath = self.ui.le_PathFile.text()
        # parser=Ctrl_FileParser()
        # self.history= parser.parseTransactionHistoryFile(filePath)
        # t=parser.history.getTransactionsByOperation("Buy")
        # print("ok")
        # self.history = parser.parseOrderHistory(filePath)

        # analyzer = Ctrl_historyAnalyzer(self.history,self.Ctrl_BinanceClient)
        # self.analyzedHistory=analyzer.getAnalyzeResults()

    def analyzeFile(self):  #TODO
        filePath = self.ui.le_PathFile.text()
        parser = Ctrl_FileParser()
        PureHistory = parser.parseTransactionHistoryFile(filePath)

        TransformedHistory=Ctrl_History().buildHistoryWithTab(PureHistory)

        if self.history==None:
            self.history=TransformedHistory
        else:
            self.history=Ctrl_History().mergeTwoHistories(self.history,TransformedHistory)
        print("ok")

        # file=self.ui.le_PathFile.text()
        # mdl_analyze=Model_BinanceReportAnalyze(file)
        # analyzer=Ctrl_historyAnalyzer(mdl_analyze)
        #
        # var = analyzer.launchAnalyze()
        # #print(file)

    def disconnectBinance(self):
        if self.Ctrl_BinanceClient is not None:
            self.Ctrl_BinanceClient.disconnect()

        self.ui.label_BinanceState.setText("Binance disconnected")


