from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from ui_output import Ui_Output
class Output(QMainWindow,Ui_Output):
    def __init__(self,server_path):
        super().__init__()
        self.server_path = server_path
        self.setupUi(self)
        with open(f"{server_path}server.log") as f:
                log = f.read()
        self.logs.setText(log)
        self.readlog()
    def readlog(self):
        while True:
            with open(f"{self.server_path}server.log") as f:
                log = f.read()
            self.logs.setText(log)