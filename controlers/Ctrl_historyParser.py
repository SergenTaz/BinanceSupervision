import csv
import pandas as pd
from BinanceSupervision.models.Model_transaction import Model_transaction
from BinanceSupervision.models.Model_transactionHistory import Model_transactionHistory

class Ctrl_historyParser():
    def __init__(self):
        self.history=Model_transactionHistory()

    def parseFile(self,path):

        if path.endswith('.csv'): #TODO
            with open(path, newline='') as file:
                spamreader = csv.reader(file, delimiter=' ', quotechar='|')
                for row in spamreader:
                    print(', '.join(row))
        elif path.endswith(".xlsx"): #TODO
            print("xlsx")
            xl_file = pd.read_excel(open(path, 'rb'))

            print(xl_file.to_numpy())

        return self.getHistory()
    def getHistory(self):
        return self.history
