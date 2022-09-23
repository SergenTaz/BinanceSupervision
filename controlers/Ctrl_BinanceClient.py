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
        self.connect(self.model.getConfig()[0],self.model.getConfig()[1])

    def updateConfig(self,config):
        self.disconnect()
        self.model.setConfig(config)
        self.connect(self.model.getConfig()[0],self.model.getConfig()[1])

    def connect(self,key,secret):
        try:
            self.client = Client(key, secret)

            self.checkBinanceConnection()
            
            info = self.client.get_account()
            for asset in self.getAccountBalance():
                print(asset['asset']+" : "+asset['free']+" - "+asset['locked'])

            #print("asset DOT: ",self.client.get_asset_balance(asset='DOT'))
            #print(self.getMarketPriceInEUR("DOT"))
            #print("history:", self.client.get_deposit_history())
            #print("ping:",self.client.get_products())
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
        logging.info("Disconnected from Binance by user")

    def getServerTime(self):
        return datetime.fromtimestamp(self.client.get_server_time()["serverTime"]/1000)

    def getMarketPriceInEUR(self,Asset):
        a=Asset.upper()+"EUR"
        return self.client.get_symbol_ticker(symbol=a)

    def getAccountBalance(self):
        balance = self.client.get_account()['balances']
        filtered=[]
        for asset in balance:
            if(float(asset['free'])!=0 or float(asset['locked'])!=0):
                filtered.append(asset)
        return filtered