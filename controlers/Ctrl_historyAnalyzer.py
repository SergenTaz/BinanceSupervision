import csv,re
import pandas as pd

from BinanceSupervision.models import Model_history
from BinanceSupervision.models.Model_AssetBalance import Model_AssetBalance
from BinanceSupervision.models.Model_BinanceReportAnalyze import Model_BinanceReportAnalyze

class Ctrl_historyAnalyzer():
    results= {}
    def __init__(self,history : Model_history, Ctrl_BinanceClient):
        self.history=history
        self.launchAnalyze(self.history,Ctrl_BinanceClient)

    def launchAnalyze(self,history,Ctrl_BinanceClient):

        for t in history:

            tokenused=t.getTokenUsed()
            amountUsed=0.0
            tokenearned=t.getTokenEarned()
            amountEarned=0.0

            if self.resultsContainsAsset(tokenused):
                if t.getType()=="BUY":
                    if tokenused=="EUR":


                        # Si le token used n'est pas EUR alors il faut récupérer la valeur en EUR du amountUsed à la date de la transaction
                        # AssetBalance du token Used : invest=invest-amountUsed(EUR)
                        # AssetBalance du token Earned : invest=invest+amountUsed(EUR)

                    # results.get(tokenused).
                    pass
                else: # transaction SELL
                    # Si le token earned n'est pas EUR alors il faut récupérer la valeur en EUR du amountUsed à la date de la transaction
                    # AssetBalance du token Used : invest=invest-amountEarned(EUR)
                    # AssetBalance du token Earned : invest=invest+amountEarned(EUR)

                    pass
            else:
                balance=Model_AssetBalance(tokenused)



    def getAnalyzeResults(self):
        return self.results

    def resultsContainsAsset(self,asset):
        if self.results.keys().__contains__(asset):
            return True
        else:
            return False

    def analyzeTransaction(self,t):
        amountEarned = 0.0
        amountUsed = 0.0
        if t.getType()=="BUY":
            if t.getTokenUsed() =="EUR":
                amountUsed=t.getAmountUsed()
            else:
                amountUsed=self.convertAmountIntoEuro(t.getTokenUsed(),t.getAmountUsed())
        elif t.getType()=="SELL":
            if t.getTokenEarned() == "EUR":
                amountEarned=t.getAmountEarned()
            else:
                amountEarned=self.convertAmountIntoEuro(t.getTokenUsed(),t.getAmountUsed())


        if not self.resultsContainsAsset(t.getTokenUsed()):
            self.results[t.getTokenUsed()]=Model_AssetBalance(t.getTokenUsed())

        if not self.resultsContainsAsset(t.getTokenEarned()):
            self.results[t.getTokenEarned()]=Model_AssetBalance(t.getTokenEarned())



    def convertAmountIntoEuro(self,tokenUsed,amountUsed):
        if self.resultsContainsAsset(tokenUsed):
            balance=self.results.get(tokenUsed)
            return ((amountUsed/balance.getQuantity())*balance.getInvest())
        else:
            return 0.0
