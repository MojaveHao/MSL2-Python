import webbrowser as web

from PySide6.QtWidgets import *

from .ui_help import Ui_Dialog


class Help(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pbtn_visit.clicked.connect(self.open_help)
        self.pbtn_exit.clicked.connect(self.quit)
    
    def open_help(self):
        temp = int(self.ledit_no.text())
        if temp == 1:
            web.open("https://minecraft.fandom.com/zh/wiki/Server.properties")
        elif temp == 2:
            web.open("https://klpbbs.com/thread-31208-1-1.html")
        elif temp == 3:
            QMessageBox.information(self, "信息", "正在整理中!")
        elif temp == 4:
            web.open("https://klpbbs.com/thread-31209-1-1.html")
        elif temp == 5:
            QMessageBox.information(self, "信息", "正在整理中!")
        elif temp == 6:
            web.open(
                "https://minecraft.fandom.com/zh/wiki/%E6%95%99%E7%A8%8B/%E4%BF%AE%E5%A4%8DApache_Log4j2%E6%BC%8F%E6%B4%9E")
        else:
            QMessageBox.warning(self, "警告", "请输入正确的序号")
    
    def quit(self):
        exit()
