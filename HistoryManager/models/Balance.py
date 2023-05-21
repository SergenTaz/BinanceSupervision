from BinanceSupervision.HistoryManager.models.History import History

class Balance():
    def __init__(self, token = "None", amount = float(0), transactionHistory : History = History()):
        self.token=token
        self.amount=amount
        self.history = transactionHistory

    def __str__(self):
        return str(self.amount) + self.token + "\n" + self.history.__str__()