import sys


from controlers.HistoryAnalyzer import HistoryAnalyzer
from controlers.HistoryParser import *
from controlers.DBWriter import *

if __name__ == '__main__':
    history=History()
    historyParser=HistoryParser()
    historyAnalyzer=HistoryAnalyzer()
    #dbWriter=DBWriter()

    file="C:\\Users\\FNRG0095\\OneDrive - orange.com\\Documents\\Perso\\part-00000-b0a9d953-9fb1-422d-b417-b3f94ab5cb58-c000.csv"

    historyParser.parse(file,history)
    print(history.__str__())

    #dbWriter.writeHistory(history)


    sys.exit(0)