import csv
import pandas as pd

from BinanceSupervision.HistoryManager.models.History import *


class HistoryParser():
    def __init__(self):
        pass

    def parse(self, path:str, history: History):
        if path.endswith('.csv'):  # TODO
            with open(path, newline='') as file:
                dialect = csv.Sniffer().sniff(file.read(1024), delimiters=";,")
                file.seek(0)
                spamreader = csv.reader(file, dialect)

                header = spamreader.__next__()
                userIDindex = header.index("User_ID")
                dateIndex = header.index("UTC_Time")
                operationIndex = header.index("Operation")
                accountIndex = header.index("Account")
                coinIndex = header.index("Coin")
                changeIndex = header.index("Change")

                for row in spamreader:
                    userID = row[userIDindex]
                    date = row[dateIndex]
                    account = row[accountIndex]
                    operation = row[operationIndex]
                    coin = row[coinIndex]
                    change = row[changeIndex]

                    history.addTransaction(Transaction(userID,date,account,operation,coin,float(change)))

        elif path.endswith(".xlsx"):  # TODO
            print("xlsx")
            xl_file = pd.read_excel(open(path, 'rb'))

            for l in xl_file.to_numpy():
                print(l)
            print(xl_file.to_numpy())


