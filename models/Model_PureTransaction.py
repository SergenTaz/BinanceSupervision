from datetime import datetime

class Model_PureTransaction:
    def __init__(self, time, account,operation,coin,change):
        if (type(time) == str):
            self.time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        else:
            self.time = time

        self.account = account
        self.operation = operation
        self.coin = coin
        self.change = change

    def __str__(self):
        return (self.time.strftime("%d/%m/%Y %H:%M:%S")+" | "+self.account+" : "+
                self.operation + self.coin + self.change)

    def getOperation(self):
        return self.operation

    def getCoin(self):
        return self.coin

    def getChange(self):
        return self.change

    def getAccount(self):
        return self.account