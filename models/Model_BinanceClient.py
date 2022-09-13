
class Model_BinanceClient():
    def __init__(self,config):
        self.config=config

    def getConfig(self):
        return self.config.getConfig()

    def setConfig(self, config):
        self.config=config

    def setServerStatus(self,status):
        #status=0 means ok but status=1 means server maintenance
        self.serverStatus=status

    def getServerStatus(self):
        return self.serverStatus