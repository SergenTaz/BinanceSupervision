from BinanceSupervision.models.Model_transaction import Model_transaction

class Model_transactionHistory():
    def __init__(self):
        self.history= []

    def addTransaction(self, transaction: Model_transaction):
        self.history.append(transaction)

    def getHistorySortedByDate(self):
        tmp=[]
        for transaction in self.history:
            tmp.append(transaction.getDate())

        tmp.sort()
        sortedList=[]
        for date in tmp:
            i=0
            while date!=self.history[i].getDate() or i>len(self.history):
                i+=1
            if i>len(self.history):
                print("ERROR transaction date not found")
            else:
                sortedList.append(self.history[i])

        self.history=sortedList

        return self

    def __str__(self):
        for transaction in self.history:
            print(transaction.__str__())