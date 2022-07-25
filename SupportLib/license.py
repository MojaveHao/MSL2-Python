import os
import webbrowser as web

from PySide6.QtWidgets import *

from .ui_license import Ui_License


class License(QDialog, Ui_License):
    def __init__(self):
        self.pbtn_quit.clicked.connect(exit)
        self.pbtn_chinese.clicked.connect(self.view_chinese)
        self.pbtn_open_file.clicked.connect(self.open_file)
        self.setupUi(self)
        self.exec()
    
    '''def quit(self):
        raise InterruptedError'''
    
    def view_chinese(self):
        web.open("https://www.chinasona.org/gnu/agpl-3.0-cn.html")
    
    def open_file(self):
        web.open("file://" + os.path.realpath("../LICENSE.txt"))
