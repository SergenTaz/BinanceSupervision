import hashlib
import hmac
import logging
import os
from urllib.parse import urlencode

from binance.client import Client
from binance.exceptions import BinanceAPIException
from datetime import datetime

from binance.helpers import round_step_size

amount = 0.000234234
tick_size = 0.00001
rounded_amount = round_step_size(amount, tick_size)

class Ctrl_BinanceClient():
    def __init__(self,model):
        self.model=model
        key,secret=model.getConfig()
        self.connect()

    def updateConfig(self,config):
        self.disconnect()
        self.model.setConfig(config)
        self.connect()

    def connect(self):
        try:

            #self.client = Client(key, secret)
            #self.client = Client("zbCOHvPXUp6s3ZyRjg5q25WmiLybOXevSCfgOyAIYRBH5kmWlrneCvB80Cf1UR7x", "9g5eE8BC9uewvgIJ0gRfGLvzr3iGBhsMQXNraYptB7iIbkg7Svu0oGh97Af32nYN")
            self.client = Client("CvAXhDl3RTADDSpNk58c7wCurEsnWUioIRn8wzkcd5sJQ6XJyqODGmx7Ashry3bg",
                                 "uP60zKQj71nvBaibCzlfAWv2aIjTK0oBeNiYU2xZQmgkamubJUqvfEVKLKtZ4rqv")

            self.checkBinanceConnection()
            
            info = self.client.get_account()
            deposit_history=self.client.get_deposit_history()
            print("account:",info["balances"][0])
            #print(self.getMarketPriceInEUR("DOT"))
            print("history:", type(self.client.get_deposit_history()))
            print("ping:",self.client.get_products())
        except BinanceAPIException as e:
            error=(str(e.status_code)+" : "+str(e.message))
            print ("Error "+error)
            print("request : "+str(e.request.url))
            logging.error(error)
            self.disconnect()

    def checkBinanceConnection(self):
        # Get server status
        self.model.setServerStatus(self.client.get_system_status()["status"])
        if self.model.getServerStatus() == 0:
            logging.info("Connected to Binance")
        else:
            logging.error("Server Maintenance")

    def disconnect(self):
        self.client.close_connection()
        logging.info("Disconnected from Binance")

    def getServerTime(self):
        return datetime.fromtimestamp(self.client.get_server_time()["serverTime"]/1000)

    def getMarketPriceInEUR(self,Asset):
        a=Asset.upper()+"EUR"
        return self.client.get_symbol_ticker(symbol=a)