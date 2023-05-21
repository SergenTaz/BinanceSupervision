from datetime import datetime

#This class modelize a transaction
class Transaction():
    def __init__(self, userID, date, account, operation: str, token, amount: float):
        self.userID=userID

        if (type(date) == str):
            self.date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        else:
            self.date = date

        self.account = account
        self.operation=operation
        self.token=token
        self.amount=amount

    def getUserid(self):
        return self.userID

    def getDate(self):
        return self.date.strftime("%d/%m/%Y %H:%M:%S")

    def getAccount(self):
        return self.account

    def getOperation(self):
        return self.operation

    def getToken(self):
        return self.token

    def getAmount(self):
        return self.amount

    def __str__(self):
        return (self.userID + " | " + self.date.strftime("%d/%m/%Y %H:%M:%S") + " | " + self.account + " | " + str(
                self.amount) + " | " + self.token + " | " + self.operation)

    def __repr__(self):
        return self.__str__()