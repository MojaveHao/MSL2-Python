from PySide6.QtCore import *
from PySide6.QtWidgets import *

from SupportLib.ui_output import Ui_Output


class Output(QDialog, Ui_Output):
    def __init__(self, server_path, stat):
        super().__init__()
        self.setupUi(self)
        self.exec()
        if stat == True:
            self.server_path = server_path
            path = self.server_path
            self.read_logs = ReadingLogs(self.server_path)
            reading = QThread.start(self.read_logs)
        else:
            QMessageBox.warning(self, "警告", "请先开启服务器")


class ReadingLogs(QThread):
    def __init__(self, path):
        super().__init__()
        self.path = path
    
    def run(self, path):
        jump = 0
        while True:
            with open(f"{path}server.log") as f:
                if jump > 0:
                    for i in range(jump):
                        f.next()
                    try:
                        for whe in range(1, 50):
                            new_logs = f.readline()
                    except:
                        jump = whe
                else:
                    for whe in range(1, 50):
                        new_logs = f.readline()
            self.new_logs = new_logs
            self.show_logs.setText(self.new_logs)
