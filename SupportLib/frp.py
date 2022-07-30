from PySide6.QtWidgets import *
import base64
import os
import random
import requests
import time
import webbrowser

from PySide6.QtWidgets import *

from .ui_frp import Ui_FrpcConfig


class FRP(QDialog, Ui_FrpcConfig):
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.exec()

        if os.path.isdir("frp"):
            pass
        else:
            os.system(
                "wget -o frp.tar.gz https://github.com/fatedier/frp/releases/download/v0.39.1/frp_0.39.1_linux_amd64.tar.gz")
            os.system("mkdir frp")
            os.system("cd frp")
            os.system("tar -zxvf frp.tar.gz")
        self.remote_port = random.randint(20000, 60000)
        # self.pbtn_start.clicked.connect(self.start)
        # self.passwd.setEnabled(False) #当付费节点维护完成之后去掉此行
        self.url_list = ["gz1.qwq.one", "sh.qwq.one", "hk.qwq.one", "hz.qwq.one", "gz2.qwq.one"]
    
    def start(self):
        url_index = self.select_url.currentIndex()
        if url_index >= 4:
            QMessageBox.Warning(self, "警告", "付费节点正在维护,请先使用免费节点")
        url = self.url_list[url_index]
        wdt = requests.get(url)
        self.token = base64.encodebytes(wdt.encode('utf8'))
        accont = self.accont.text()
        passwd = self.passwd.text()
        port = self.port.text()
        write = f"[common]\n\
server_port=7000\n\
server_addr={url}\n\
token={self.token}\n\
\n\
[{accont}]\n\
type=tcp\n\
local_ip=127.0.0.1\n\
local_port={port}\n\
remote_port="
        with open("./frp/frpc.ini", "w") as f:
            f.write(write)
        os.system("cd frp || ./frpc -c frpc.ini")
    
    def buy_vip(self):
        webbrowser.oepn("https://www.afdian.net/@makabaka123")
    
    def check_update(self):
        api_url = 'https://api.github.com/repos/fatedier/frp'
        result = requests.get(api_url).json()
        date = result['updated_at']
        fmt_date = time.mktime(time.strptime(date, "%Y-%m-%dT%H:%M:%S"))
        files = os.listdir("frp")
        get_time = os.path.getmtime("./frp/LICENCE")
        if not get_time:
            get_time = date
        if get_time < date:
            os.system("wget -o frp.zip https://github.com/fatedier/frp/archive/master.zip")
        os.system("python update_frp.py")
        exit()
