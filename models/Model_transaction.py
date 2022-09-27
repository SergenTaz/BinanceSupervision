
class Model_transaction():
    def __init__(self, date,transaction_type: str, amount_used: float, amount_received: float):
        self.date=date
        self.transaction_type=transaction_type
        self.amount_used=amount_used
        self.amount_received=amount_received

    def getDate(self):
        return self.date

    def getType(self):
        return self.transaction_type

    def getAmountUsed(self):
        return self.amount_used

    def getAmountReceived(self):
        return self.amount_received