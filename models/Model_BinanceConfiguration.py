
class Model_BinanceConfiguration():
    def __init__(self):
        pass

    def setApiKey(self,key):
        self.apiKey=key

    def setApiSecret(self,secret):
        self.apiSecret=secret

    def getConfig(self):
        return self.apiKey,self.apiSecret
