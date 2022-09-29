import csv
import pandas as pd
from BinanceSupervision.models.Model_transaction import Model_transaction
from BinanceSupervision.models.Model_history import Model_History
from BinanceSupervision.models.Model_transaction import Model_transaction

class Ctrl_historyParser():
    def __init__(self, history):
        if history==None:
            self.history=Model_History()
        else:
            self.history=history

    def parseFile(self,path):

        if path.endswith('.csv'): #TODO
            with open(path, newline='') as file:
                dialect = csv.Sniffer().sniff(file.read(1024), delimiters=";,")
                file.seek(0)
                spamreader = csv.reader(file, dialect)

                header = spamreader.__next__()
                dateIndex = header.index("UTC_Time")
                operationIndex = header.index("Operation")
                accountIndex = header.index("Account")
                coinIndex = header.index("Coin")
                changeIndex= header.index("Change")

                for row in spamreader:

                    date = row[dateIndex]
                    operation=row[operationIndex]
                    amount=float(row[changeIndex])
                    tokenearned=""
                    amountearned=0
                    tokenused=""
                    amountused=0

                    if(operation=="Buy"):                                                                   #If the action is a buy
                        if(amount>float(0)):                                                                #If it is the amount earned
                            tokenearned=row[coinIndex]
                            amountearned=amount
                            next = spamreader.__next__()
                            if next[operationIndex]=="Fee":
                                next = spamreader.__next__()
                            tokenused = next[coinIndex]
                            amountused = abs(float(next[changeIndex]))
                        else:                                                                               #If it is the amount used to buy
                            tokenused=row[coinIndex]
                            amountused = abs(amount)
                            next = spamreader.__next__()
                            if next[operationIndex]=="Fee":
                                next = spamreader.__next__()
                            tokenearned = next[coinIndex]
                            amountearned = float(next[changeIndex])

                        self.history.addTransaction(Model_transaction(date, operation,tokenused,amountused,tokenearned,amountearned))

        elif path.endswith(".xlsx"): #TODO
            print("xlsx")
            xl_file = pd.read_excel(open(path, 'rb'))

            for l in xl_file.to_numpy():
                print(l)
            print(xl_file.to_numpy())

        return self.getHistory()

    def readDB(self):   #TODO
        pass

    def getHistory(self):
        return self.history.gettransactionHistorySortedByDate()
