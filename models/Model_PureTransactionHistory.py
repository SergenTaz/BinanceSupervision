from BinanceSupervision.models.Model_PureTransaction import Model_PureTransaction

class Model_PureTransactionHistory:
    def __init__(self):
        self.history=[]

    def addTransaction(self,t: Model_PureTransaction):
        if not(self.alreadyExist(t)):
            self.history.append(t)

    def alreadyExist(self,transaction: Model_PureTransaction):
        for t in self.history:
            if t.__str__()==transaction.__str__():
                return True
        return False

    def getTransactionsByOperation(self,operation):
        res=[]
        for t in self.history:
            if t.getOperation()==operation:
                res.append(t)
        return res