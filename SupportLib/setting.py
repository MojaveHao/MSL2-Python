from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from ui_setiing import Ui_Setting
import webbrowser as web
import os
class Setting(QDialog,Ui_Setting):
    def __init__(self):
        self.update_setting = 'Master'
        self.website_list = ['https://files.minecraftforge.net/net/minecraftforge/forge/','https://fabricmc.net/','https://getbukkit.org/download/craftbukkit','https://getbukkit.org/download/spigot','https://getbukkit.org/download/vanilla']
        self.pbtn_ufl1clicked.connect(self.open_uft1)
        self.pbtn_ufl2.clicked.connect(self.open_uft2)
        self.pbtn_download_auto_backup.clicked.connect(self.auto_backup)
        self.pbtn_download_website_manage.clicked.connect(self.web_mang)
        self.pbtn_goto.clicked.connect(self.goto)
        self.pbtn_check_configs_for_server.clicked.connect(self.check_all_configs)
        self.dl_update.clicked.connect(self.download_update)
        with open('../config.txt') as f:
            self.path = f.read()[0][0]
    def open_uft1(self):
        web.open('https://wiki.biligame.com/rust/%E6%9C%8D%E4%B8%BB:%E5%B8%B8%E7%94%A8%E6%8F%92%E4%BB%B6')
    def open_uft2(self):
        web.open('https://www.bilibili.com/read/cv341114')
    def auto_backup(self):
        web.open('https://www.mcbbs.net/thread-957949-1-1.html')
    def web_mang(self):
        web.open('https://www.mcbbs.net/forum.php?mod=viewthread&tid=1230139')
    def goto(self):
        if 'CBukkit' in self.cbox_goto_website.text():
            web.open(self.website_list[0])
        elif 'Spigot' in self.cbox_goto_website.text():
            web.open(self.website_list[1])
        elif 'Vanilla' in self.cbox_goto_website.text():
            web.open(self.website_list[2])
        elif 'Froge' in self.cbox_goto_website.text():
            web.open(self.website_list[3])
        elif 'Fabric' in self.cbox_goto_website.text():
            web.open(self.website_list[4])
    def check_all_configs(self): 
        config_list = []
        for file in os.listdir(self.path):
            if '.xaml' in file or '.xml' in file or '.yml' in file or '.yaml' in file:
                config_list.append(file)
    def download_update(self):
        self.update_setting = self.cbox_update.text()
        if self.update_setting == 'Master':
            #下载main分支
            pass
        if self.update_setting == 'Monthly':
            #下载Monthly分支
            pass
        if self.update_setting == 'Dev':
            #下载dev分支
            pass