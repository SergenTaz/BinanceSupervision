from datetime import datetime

class Model_transaction():
    def __init__(self, date,transaction_type: str, token_used, amount_used: float, token_earned, amount_earned: float):
        if(type(date)==str):
            self.date=datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
        else:
            self.date=date
        self.transaction_type=transaction_type
        self.token_used=token_used
        self.amount_used=amount_used
        self.token_earned = token_earned
        self.amount_earned=amount_earned

    def getDate(self):
        return self.date

    def getType(self):
        return self.transaction_type

    def getAmountUsed(self):
        return self.amount_used

    def getTokenUsed(self):
        return self.token_used

    def getAmountEarned(self):
        return self.amount_earned

    def getTokenEarned(self):
        return self.token_earned

    def __str__(self):
        return (self.date.strftime("%d/%m/%Y %H:%M:%S")+" | "+self.transaction_type+ " : "+str(self.amount_earned) +" "+ self.token_earned+ " for "+ str(self.amount_used)+ " "+ self.token_used)