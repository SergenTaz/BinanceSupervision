import configparser

class Ctrl_ConfigFile():
    def __init__(self):
        pass

    def writeBinanceConfiguration(self,key,secret):
        config=configparser.ConfigParser()

        config.add_section('Binance Configuration')
        config['Binance Configuration']['API key']=key
        config['Binance Configuration']['API secret'] = secret

        try:
            with open('conf.ini', 'w') as configFile:
                config.write(configFile)
            return 1
        except:
            return 0

    def readBinanceConfiguration(self):
        key=""
        secret=""
        try:
            config=configparser.ConfigParser()
            config.read('conf.ini')
            key=config['Binance Configuration']['API key']
            secret=config['Binance Configuration']['API secret']
        except:
            pass
        return key,secret

