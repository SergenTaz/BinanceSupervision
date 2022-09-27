import csv,re
import pandas as pd

from BinanceSupervision.models.Model_BinanceReportAnalyze import Model_BinanceReportAnalyze

class Ctrl_BinanceReportAnalyzer():
    analyze=None
    def __init__(self,analyze: Model_BinanceReportAnalyze):
        self.analyze=analyze

    def launchAnalyze(self,history):
        pass


