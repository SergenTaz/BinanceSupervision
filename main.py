import os,sys,logging


from PyQt5.QtWidgets import QApplication

from BinanceSupervision.views.View_mainWindow import Window
from BinanceSupervision.models.Model_app import Model_app
from BinanceSupervision.controlers.Ctrl_mainWindow import Ctrl_mainWindow

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model_app()
        self.main_controller = Ctrl_mainWindow(self.model)
        self.main_view = Window(self.model, self.main_controller)
        self.main_view.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec())



