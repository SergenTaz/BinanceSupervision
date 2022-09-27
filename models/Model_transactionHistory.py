from Model_transaction import Model_transaction

class Model_transactionHistory():
    def __init__(self):
        self.history= []

    def addTransaction(self, transaction: Model_transaction):
        self.history.append(transaction)

    def sortHistoryByDate(self):    #TODO
        pass