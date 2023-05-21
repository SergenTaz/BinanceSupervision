import sys

from BinanceSupervision.controlers.DBReader import DBReader
from BinanceSupervision.controlers.HistoryAnalyzer import HistoryAnalyzer
from BinanceSupervision.controlers.HistoryParser import *
from BinanceSupervision.controlers.DBWriter import *

if __name__ == '__main__':
    history=History()
    historyParser=HistoryParser()
    historyAnalyzer=HistoryAnalyzer()
    dbWriter=DBWriter('192.168.1.100','root','mariadb','BinanceSupervision',3306)
    dbReader=DBReader('192.168.1.100','root','mariadb','BinanceSupervision',3306)

    file="E:\\Documents\\Thibaut Roudel\\Finances\\Crypto\\2022\\transaction-history-01-01-2022-to-31-12-2022.csv"

    historyParser.parse(file,history)
    print(history.__str__())

    dbWriter.writeHistory(history)
    dbReader.getSumDeposits()


    sys.exit(0)