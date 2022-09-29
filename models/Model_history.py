from BinanceSupervision.models.Model_transaction import Model_transaction

class Model_History():
    def __init__(self):
        self.transactionHistory= []
        self.totalInvested=0.0

    def addTransaction(self, transaction: Model_transaction):
        if not(self.alreadyExist(transaction)):
            if(transaction.getType()=="Buy" and transaction.getTokenUsed()=="EUR"):
                self.totalInvested=self.totalInvested+transaction.getAmountUsed()
            self.transactionHistory.append(transaction)

    def gettransactionHistorySortedByDate(self):
        tmp=[]
        for transaction in self.transactionHistory:
            tmp.append(transaction.getDate())

        tmp.sort()
        sortedList=[]
        for date in tmp:
            i=0
            while date!=self.transactionHistory[i].getDate() or i>len(self.transactionHistory):
                i+=1
            if i>len(self.transactionHistory):
                print("ERROR transaction date not found")
            else:
                sortedList.append(self.transactionHistory[i])
                self.transactionHistory.remove(self.transactionHistory[i])

        self.transactionHistory=sortedList

        return self

    def alreadyExist(self,transaction: Model_transaction):
        for t in self.transactionHistory:
            if t.__str__()==transaction.__str__():
                return True

        return False

    def __str__(self):
        for transaction in self.transactionHistory:
            print(transaction.__str__())
        print("Total invested : "+str(self.totalInvested)+"€")