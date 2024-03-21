from controlers.Ctrl_ConfigFile import Ctrl_ConfigFile

class Ctrl_BinanceConfiguration():

    def __init__(self,model):
        configFile=Ctrl_ConfigFile()
        key,secret=configFile.readBinanceConfiguration()
        self.model=model
        self.model.setApiKey(key)
        self.model.setApiSecret(secret)

    def OkClicked(self,apiKey,apiSecret):
        key,secret=self.model.getConfig()
        if (key!=apiKey or secret!=apiSecret):
            self.model.setApiKey(apiKey)
            self.model.setApiSecret(apiSecret)
            configFile=Ctrl_ConfigFile()
            if(configFile.writeBinanceConfiguration(apiKey,apiSecret)):
                print("Configuration saved")
            else:
                print("Failed to save configuration")
        else:
            print("No change to apply")




