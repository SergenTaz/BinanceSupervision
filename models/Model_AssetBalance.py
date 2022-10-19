class Model_AssetBalance():
    def __init__(self,symbol):
        self.symbol=symbol
        self.invest=0
        self.quantity=0

    def incrementInvest(self,amount):
        self.invest=self.invest+amount

    def decrementInvest(self,amount):
        self.invest=self.invest-amount

    def incrementQuantity(self,amount):
        self.quantity=self.quantity+amount

    def decrementQuantity(self,amount):
        self.quantity=self.quantity-amount

    def getAveragePrice(self):
        return self.invest/self.quantity
