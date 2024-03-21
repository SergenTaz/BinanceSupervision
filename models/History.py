from models.Transaction import Transaction

#This class modelize a transaction history, it stores all the transaction
class History():
    def __init__(self):
        self.history = []

    def addTransaction(self, transaction: Transaction):
        if not(self.HistoryAlreadyContainsTransaction(transaction)):
            self.history.append(transaction)

    def HistoryAlreadyContainsTransaction(self, transaction: Transaction):
        for t in self.history:
            if (t.__str__() == transaction.__str__()):
                return True
        return False

    def __str__(self):
        return self.history.__str__()

    def __repr__(self):
        return self.__str__()