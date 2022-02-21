from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from ui_output import Ui_Output
class Output(QMainWindow, Ui_Output):
    def __init__(self,server_path):
        super().__init__()
        self.server_path = server_path
        self.setupUi(self)