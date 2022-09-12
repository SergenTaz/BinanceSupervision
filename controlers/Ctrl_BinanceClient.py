from binance.client import Client
from binance.exceptions import BinanceAPIException
import datetime


class Ctrl_BinanceClient():
    def __init__(self,model):
        self.model=model
        key,secret=model.getConfig()

        try:
            #self.client = Client(key, secret)
            self.client = Client("zbCOHvPXUp6s3ZyRjg5q25WmiLybOXevSCfgOyAIYRBH5kmWlrneCvB80Cf1UR7x", "9g5eE8BC9uewvgIJ0gRfGLvzr3iGBhsMQXNraYptB7iIbkg7Svu0oGh97Af32nYN")
            print(self.client.get_server_time())
            print(datetime.datetime.fromtimestamp(self.client.get_server_time()["serverTime"]))
            self.client.close_connection()
            pass
        except BinanceAPIException as e:
            print (e.status_code)
            print (e.message)

    def updateConfig(self,config):
        self.model.setConfig(config)

