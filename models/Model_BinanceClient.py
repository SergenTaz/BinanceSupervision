
class Model_BinanceClient():
    def __init__(self,config):
        self.config=config

    def getConfig(self):
        return self.config.getConfig()