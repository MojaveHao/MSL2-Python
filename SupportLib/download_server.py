import requests
from PySide6.QtWidgets import *

from SupportLib.download import download
from SupportLib.ui_download import Ui_Dialog


class Download_Manager(QDialog, Ui_Dialog):
    def __init__(self, server_path):
        super().__init__()
        self.source = ""
        self.name = ""
        self.ver = "1.18.1"
        self.step = 0
        self.spigot_versions = ['1.18.2', '1.18.1', '1.18', '1.17.1', '1.17', '1.16.5', '1.16.4', '1.16.3', '1.16.2',
                                '1.16.1', '1.16.', '1.15.2', '1.15.1', '1.15', '1.14.4', '1.14.3', '1.14.2', '1.14.1',
                                '1.14', '1.13.2', '1.13.1', '1.13', '1.12.2', '1.12.1', '1.12', '1.11.2', '1.11.1',
                                '1.11', '1.10.2', '1.10.1', '1.10', '1.9.4', '1.9.3', '1.9.2', '1.9.1', '1.9', '1.8.8',
                                '1.8.7', '1.8.6', '1.8.5', '1.8.4', '1.8.3', '1.8.2', '1.8.1', '1.8', '1.7.10', '1.7.9',
                                '1.7.8', '1.7.7', '1.7.6', '1.7.5', '1.7.4', '1.7.3', '1.7.2', '1.7.1', '1.7', '1.6.4',
                                '1.6.2', '1.5.1', '1.4.7', '1.4.6']
        self.vanilla_versions = ['1.18.2', '1.18.1', '1.18', '1.17.1', '1.17', '1.16.5', '1.16.4', '1.16.3', '1.16.2',
                                 '1.16.1', '1.16.', '1.15.2', '1.15.1', '1.15', '1.14.4', '1.14.3', '1.14.2', '1.14.1',
                                 '1.14', '1.13.2', '1.13.1', '1.13', '1.12.2', '1.12.1', '1.12', '1.11.2', '1.11.1',
                                 '1.11', '1.10.2', '1.10.1', '1.10', '1.9.4', '1.9.3', '1.9.2', '1.9.1', '1.9', '1.8.8',
                                 '1.8.7', '1.8.6', '1.8.5', '1.8.4', '1.8.3', '1.8.2', '1.8.1', '1.8', '1.7.10',
                                 '1.7.9', '1.7.8', '1.7.7', '1.7.6', '1.7.5', '1.7.4', '1.7.3', '1.7.2', '1.7.1', '1.7',
                                 '1.6.4', '1.6.2', '1.6.1', '1.5.2', '1.5.1', '1.4.7', '1.4.6', '1.4.5', '1.4.4',
                                 '1.4.2', '1.3.2', '1.3.1']
        self.bukkit_versions = ['1.18.2', '1.18.1', '1.18', '1.17.1', '1.17', '1.16.5', '1.16.4', '1.16.3', '1.16.2',
                                '1.16.1', '1.16.', '1.15.2', '1.15.1', '1.15', '1.14.4', '1.14.3', '1.14.2', '1.14.1',
                                '1.14', '1.13.2', '1.13.1', '1.13', '1.12.2', '1.12.1', '1.12', '1.11.2', '1.11.1',
                                '1.11', '1.10.2', '1.10.1', '1.10', '1.9.4', '1.9.3', '1.9.2', '1.9.1', '1.9', '1.8.8',
                                '1.8.7', '1.8.6', '1.8.5', '1.8.4', '1.8.3', '1.8.2', '1.8.1', '1.8', '1.7.10', '1.7.9',
                                '1.7.8', '1.7.7', '1.7.6', '1.7.5', '1.7.4', '1.7.3', '1.7.2', '1.7.1', '1.7', '1.6.4',
                                '1.6.2', '1.6.1', '1.5.2', '1.5.1', '1.4.7', '1.4.6', '1.4.5', '1.4.4', '1.4.2',
                                '1.3.2', '1.3.1', '1.2.5', '1.2.4', '1.2.3', '1.2.2', '1.1', '1.0']
        self.paper_versions = ['1.18.1-216', '1.18-66', '1.17.1-409', '1.17-79', '1.16.5-794', '1.16.4-416',
                               '1.16.3-253', '1.16.2-189', '1.16.1-138', '1.15.2-393', '1.15.1-62', '1.15-21',
                               '1.14.4-245', '1.14.3-134', '1.14.2-107', '1.14.1-50', '1.14-17', '1.13.2-657',
                               '1.13.1-386', '1.13-173', '1.12.2-1620', '1.12.1-1204', '1.12-1169', '1.11.2-1106',
                               '1.10.2-918', '1.9.4-775', '1.8.8-445']
        self.purpur_versions = ['1.18.1-1556', '1.18-1433', '1.17.1-1428', '1.17-1255', '1.16.5-1171', '1.16.4-956',
                                '1.16.3-808', '1.16.2-750', '1.16.1-710', '1.16', '1.15.2-606', '1.15.1-397',
                                '1.15-346', '1.14.4-337', '1.14.3-202', '1.14.2-126', '1.14.1-63']
        self.server_path = server_path
        self.setupUi(self)
        self.pbtn_ok1(self.set_type)
        self.pbtn_ok2(self.set_version)
        self.show()
    
    def set_source(self):
        self.source = self.cbox_source.currentText()
        if "Xiaoyu" in self.source:
            self.cbox_type.clear()
            self.cbox_type.add("Bugjump(Mojang)")
            self.cbox_type.add("Loliserver")
            self.cbox_type.add("Arclight")
            self.cbox_type.add("Catserver")
            self.cbox_type.add("Paper")
            self.cbox_type.add("Purpur")
        elif "Sakura" in self.source:
            pass
        else:
            self.cbox_type.clear()
            self.cbox_type.add("Spigot")
            self.cbox_type.add("Vanilla")
            self.cbox_type.add("Bukkit")
        self.step += 1
    
    def set_version(self):
        if self.step == 1:
            self.type = self.cbox_type.currentText()
            if self.type == "Bugjump(Mojang)":
                self.cbox_ver.clear()
                self.cbox_ver.addItem("1.18.1")
                self.cbox_ver.addItem("1.17.1")
                self.cbox_ver.addItem("1.17")
                self.cbox_ver.addItem("1.16.5")
                self.cbox_ver.addItem("1.15.2")
                self.cbox_ver.addItem("1.14.4")
                self.cbox_ver.addItem("1.13.2")
                self.cbox_ver.addItem("1.12.2")
                self.cbox_ver.addItem("1.11.2")
                self.cbox_ver.addItem("1.10.2")
                self.cbox_ver.addItem("1.9.4")
                self.cbox_ver.addItem("1.8.9")
                self.cbox_ver.addItem("1.7.0")
                resource = requests.get("https://dwmcs.nstarmc.cn/version.json")
                temp1 = eval(resource)
                self.temp2 = temp1[0]
            if self.type == "Loliserver":
                self.cbox_ver.clear()
                self.cbox_ver.addItem("1.16.5")
                self.temp2 = temp1[1]
            if self.type == "Arclight":
                self.cbox_ver.clear()
                self.cbox_ver.addItem("1.16.5")
                self.cbox_ver.addItem("1.15.2")
                self.temp2 = temp1[1]
            if self.type == "Caterver":
                self.cbox_ver.clear()
                self.cbox_ver.addItem("1.12.2")
                self.temp2 = temp1[1]
            if self.type == "Spigot":
                self.cbox_ver.clear()
                for item in self.spigot_versions:
                    self.cbox_ver.addItem(item)
            if self.type == "Vanilla":
                self.cbox_ver.clear()
                for item in self.vanilla_versions:
                    self.cbox_ver.addItem(item)
            if self.type == "Bukkit":
                self.cbox_ver.clear()
                for item in self.bukkit_versions:
                    self.cbox_ver.addItem(item)
            if self.type == "Purpur":
                self.cbox_ver.clear()
                for item in self.purpur_versions:
                    self.cbox_ver.addItem(item)
            if self.type == "Paper":
                self.cbox_ver.clear()
                for item in self.paper_versions:
                    self.cbox_ver.addItem(item)
        else:
            QMessageBox.warning(self, "警告", "您必须先选择下载源")
        self.step += 1
    
    def download(self):
        if self.step == 2:
            self.ver = self.cbox_ver.currentText()
            if self.type == 'Bugjump(Mojang)':
                temp = self.cbox_ver.currentIndex()
                download(down_url=self.temp2[temp], down_name='server.jar', down_path='../MSLDownload/')
            if self.type == 'Loliserver':
                download(down_url=self.temp2[0], down_name='LoliServer-1.16.5-185-server.jar', down_path='../MSLDownload/')
            if self.type == 'Arclight':
                if self.ver == '1.16.5':
                    download(down_url=self.temp2[1], down_name='arclight-forge-1.16-1.0.18.jar', down_path='../MSLDownload/')
                if self.ver == '1.15.2':
                    download(down_url=self.temp2[2], down_name='arclight-forge-1.15-1.0.18.jar', down_path='../MSLDownload/')
            if self.type == 'Catserver':
                download(self.temp2[3], down_name='arclight-forge-1.16-1.0.18.jar', down_path='../MSLDownload/')
            if self.type == 'Spigot':
                download(down_url=f'https://download.getbukkit.org/spigot/spigot-{self.ver}.jar', down_name=f'Spigot-{self.ver}.jar',
                         down_path='../MSLDownload/')
            if self.type == 'Vanilla':
                download(down_url=f'https://download.getbukkit.org/vanilla/vanilla-{self.ver}.jar', down_name=f'Vanilla-{self.ver}.jar',
                         down_path='../MSLDownload/')
            if self.type == 'Bukkit':
                download(down_url=f'https://download.getbukkit.org/spigot/craftbukkit-{self.ver}.jar',down_name=
                         f'CraftBukkit-{self.ver}.jar', down_path='../MSLDownload/')
            if self.type == 'Purpur':
                download(down_url=f'https://https://dwmcs.nstarmc.cn/Purpur/purpur-{self.ver}', down_name= f'Purpur-{self.ver}.jar',
                         down_path='../MSLDownload/')
            if self.type == 'Paper':
                download(down_url=f'https://https://dwmcs.nstarmc.cn/Paper/paper-{self.ver}',down_name= f'Paper-{self.ver}.jar',
                         down_path='../MSLDownload/')
        else:
            QMessageBox.warning(self, "警告", "您必须先选择服务端")
