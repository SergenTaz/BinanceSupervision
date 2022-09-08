from BinanceSupervision.views.View_BinanceConfiguration import Dialog

class Ctrl_BinanceConfiguration():

    def __init__(self,model):
        self.model=model

    def OkClicked(self,apiKey,apiSecret):
        self.model.setApiKey(apiKey)
        self.model.setApiSecret(apiSecret)


