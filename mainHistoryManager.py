import sys

from controlers.DBReader import DBReader
from controlers.HistoryAnalyzer import HistoryAnalyzer
from controlers.HistoryParser import *
from controlers.DBWriter import *
from controlers.Ctrl_ConfigFile import Ctrl_ConfigFile

if __name__ == '__main__':
    configFile = Ctrl_ConfigFile()
    url, port, user, pwd, db = configFile.readDBConfiguration()


    # history=History()
    # historyParser=HistoryParser()
    # historyAnalyzer=HistoryAnalyzer()
    # dbWriter=DBWriter(url,user,pwd,db,port)
    dbReader=DBReader(url,user,pwd,db,int(port))

    # file="E:\\Documents\\Thibaut Roudel\\Finances\\Crypto\\2022\\transaction-history-01-01-2022-to-31-12-2022.csv"

    # historyParser.parse(file,history)
    # print(history.__str__())

    # dbWriter.writeHistory(history)
    # print(dbReader.getSumDeposits())
    for row in dbReader.getCoinHistory("EUR"):
        print(row)


    sys.exit(0)

