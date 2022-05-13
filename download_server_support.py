from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from SupportLib.cmdl_get_server import get_file_url
from SupportLib.download import download
from SupportLib.ui_download import Ui_Dialog


class Download_Manager(QDialog, Ui_Dialog):
    def __init__(self, server_path):
        super().__init__()
        self.download_type = ""
        self.server_path = server_path
        self.setupUi(self)
        self.pbtn_start_download.clicked.connect(self.download)
        self.show()

    def download(self):
        type = self.cbox_type.currentText()
        version = self.comboBox.currentText()
        url, name = get_file_url(type, version)
        download(url, name, download_path=self.server_path)
        print("请等待在弹出的窗口中下载文件,下载完成后将存放在MSLDownload目录下")
