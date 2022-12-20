import os
import subprocess as sp
import sys
import webbrowser as web

from PySide6.QtGui import *
from PySide6.QtWidgets import *
from tqdm import tqdm

import SupportLib.RAM as RAM
from SupportLib.create_config import *
#from SupportLib.download_server_support import Download_Manager as DManager
from SupportLib.frp import FRP
from SupportLib.Output import Output
from SupportLib.setting import Setting
from SupportLib.ui_kfq import Ui_MainWindow as MSL2Py

# from SupportLib.mslhelp import Help
# from SupportLib.license import License

class MSL2(QMainWindow, MSL2Py, Output, FRP, Setting):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.debug_mode = 1
        with tqdm(total=36) as pbar:
            pbar.set_description('pyMSL:SettingUp')
            self.setWindowIcon(QIcon("Resource" + os.sep + "logo.png"))
            pbar.update(1)
            self.setWindowTitle("pyMSL 22M12 Release 1")
            pbar.update(1)
            self.using_java = 3  # 0为17，1为16，2为8，3为使用系统变量
            pbar.update(1)
            self.want_to_download = 0  # 同上
            pbar.update(1)
            self.java_path = ["/usr/lib/jvm/java-17-openjdk-amd64/", "/usr/lib/jvm/java-16-openjdk-amd64/",
                              "/usr/lib/jvm/java-8-openjdk-amd64/", '']
            pbar.update(1)
            self.server_path = ""  # 服务端的路径
            pbar.update(1)
            self.server_name = "server.jar"  # 服务端的名字，需要单独设置
            pbar.update(1)
            self.min_mem_G = 1  # 最小内存(G)
            pbar.update(1)
            self.max_mem_G = int(RAM.mem()[1] / 1000000000)  # 最大内存(G)
            pbar.update(1)
            self.dis_log4j2 = True  # 是否禁用log4j2
            pbar.update(1)
            self.online_mode = True  # 是否开启正版验证
            pbar.update(1)
            self.max_players = 20  # 最大玩家数量
            pbar.update(1)
            self.serv_port = 19132  # 服务器端口
            pbar.update(1)
            self.pvp = True  # 开启PVP
            pbar.update(1)
            self.command_block = True  # 开启命令方块
            pbar.update(1)
            self.motd_message = "Welcome!"  # 服务器选择界面提示
            pbar.update(1)
            self.select_card = 0  # 打开的选项卡，0为无，1为日志，2为映射，3为关于
            pbar.update(1)
            self.server_status = False  # 服务器状态，False为关闭，True为开启
            pbar.update(1)
            self.server_start_opitions = ""
            pbar.update(1)
            self.pbtn_output.setIcon(QIcon("Resource" + os.sep + "Book.gif"))  # 设置输出摁钮的图案为书
            pbar.update(1)
            self.pbtn_frp.setIcon(QIcon("Resource" + os.sep + "Furnace.png"))  # 设置内网穿透摁钮的图案为熔炉
            pbar.update(1)
            self.pbtn_about.setIcon(QIcon("Resource" + os.sep + "Quill.png"))  # 设置关于摁钮的图案为书和笔
            pbar.update(1)
            self.pbtn_ok_adv_set.clicked.connect(self.set_adv)  # 此行开始直到第95行都是绑定摁钮处理方法
            pbar.update(1)
            self.pbtn_dis_log4j2.clicked.connect(self.process_log4j2)
            pbar.update(1)
            self.pbtn_start_server.clicked.connect(self.start_server)
            pbar.update(1)
            self.pbtn_about.clicked.connect(self.about)
            pbar.update(1)
            self.pbtn_output.clicked.connect(self.open_logs)
            pbar.update(1)
            self.pbtn_show_java_path.clicked.connect(self.show_java_path)
            pbar.update(1)
            self.pbtn_select_path.clicked.connect(self.select_server_path)
            pbar.update(1)
            self.pbtn_download_server.clicked.connect(self.download_server)
            pbar.update(1)
            self.pbtn_frp.clicked.connect(self.frp_guide)
            pbar.update(1)
            self.pbtn_visit_help.clicked.connect(self.visit_help)
            pbar.update(1)
            self.pbtn_upd_set.clicked.connect(self.open_set)
            pbar.update(1)
        
            if not os.path.isdir("MSLDownload"):  # 判断是否有下载目录，没有就创建
                os.mkdir("MSLDownload")
            else:
                self.download_path = "../MSLDownload"
            pbar.update(1)
            
            self.glob_conf = {'Server_Name':f'{self.server_name}','Server_Path':f'{self.server_path}','Java_Path':f'{self.java_path[self.using_java]}','Min_Mem':f'{self.min_mem_G}','Max_Mem':f'{self.max_mem_G}','Port':f'{self.serv_port}',}
            pbar.update(1)
            
            if os.path.isfile("msl_config.txt"):  # 如果存在配置就从配置读取
                config = read_config()
                self.server_name = config['Server_Name']
                self.server_path = config['Server_Path']
                self.java_path = config['Java_Path']
                self.min_mem_G = config['Min_Mem']
                self.max_mem_G = config['Max_Mem']
                self.serv_port = config['Port']
                self.using_java = 3
                
            else: # 不存在配置就写入
                
                write_config(self.glob_conf)

            pbar.update(1)
    def set_adv(self):  # 读写server.properties文件修改设置
        if not self.server_status:
            with tqdm(total=7) as pbar:
                pbar.set_description('pyMSL:ReadingServerConfig')
                self.min_mem_G = self.min_ram.value()  # 获取最小内存(G)
                pbar.update(1)
                self.max_mem_G = self.max_ram.value()  # 获取最大内存(G)
                pbar.update(1)
                if self.min_mem_G > self.max_mem_G:
                    QMessageBox.warning(self,"警告","最小内存大于最大内存，请修改")
                self.max_players = int(self.max_player.text())  # 获取最大玩家数量
                print(self.max_players)
                pbar.update(1)
                self.serv_port = int(self.server_port.text())  # 获取服务器端口
                print(self.serv_port)
                pbar.update(1)
                self.pvp = bool(self.cbox_pvp)  # 获取是否启用pvp
                pbar.update(1)
                self.command_block = bool(self.cbox_command_block)  # 获取是否启用命令方块
                pbar.update(1)
                self.motd_message = self.motd.text()  # 设置服务器选择界面的提示
                pbar.update(1)
            if os.path.isdir(self.server_path):  # 如果服务端路径存在就执行
                try:
                    with open(f"{self.server_path}" + os.sep + "server.properties", encoding='utf-8') as f:  # 读取server.properties
                        server_lines = f.readlines()
                except:
                    QMessageBox.warning(self, "警告", "您必须确保已经在服务端路径下生成了server.properties文件")
                for i in range(len(server_lines)):  # 遍历server.properties，并且在内存中修改内容
                        if "max-players=" in server_lines[i]:
                            server_lines[i] = f"max-players={self.max_players}\n"
                        if "server-port=" in server_lines[i]:
                            server_lines[i] = f"server-port={self.serv_port}\n"
                        if "pvp=" in server_lines[i]:
                            server_lines[i] = f"pvp={self.pvp}\n"
                        if "enable-command-block=" in server_lines[i]:
                            server_lines[i] = f"enable-command-blocks={self.command_block}\n"
                print(server_lines)
                with open(f"{self.server_path}" + os.sep + "server.properties", "w", encoding='utf-8') as f:  # 将修改后的内容重新写回server.properties
                    f.writelines(server_lines)
            else:
                QMessageBox.warning(self, "警告", "请您选择正确的服务端路径")
            self.min_ram.setMinimum(1)  # 定义最小内存为1G
            self.min_ram.setMaximum(self.max_mem_G)  # 设置最大内存
            self.max_ram.setMinimum(self.min_mem_G)  # 设置最小内存
            write_config(self.glob_conf)
        else:
            QMessageBox.warning(self, "警告", "请您在关闭服务器后再更改此部分设置!")
    
    def process_log4j2(self):
        self.dis_log4j2 = not self.dis_log4j2  # 反相是否启用log4j2的设置
        if self.dis_log4j2:  # 设置反相之后摁钮显示的文字
            self.pbtn_dis_log4j2.setText("启用log4j2 (不推荐)")
            self.server_start_opitions += "-Dlog4j2.formatMsgNoLookups=true"
        else:
            self.pbtn_dis_log4j2.setText("通过启动参数禁用Log4j2")
            self.server_start_opitions.replace("-Dlog4j2.formatMsgNoLookups=true", '')
    
    def start_server(self):  # 启动服务器
        self.using_java = self.cbox_using_java.currentIndex()
        print(['java','-jar',f'-Xms{self.min_mem_G}G',f'-Xmx{self.max_mem_G}G',f'{self.server_name}',f'{self.server_start_opitions}'],f"cwd:{self.server_path}")
        sp.run(['java','-jar',f'-Xms{self.min_mem_G}G',f'-Xmx{self.max_mem_G}G',f'{self.server_name}',f'{self.server_start_opitions}'],cwd=self.server_path,check=True,shell=True,stdout=open('latest.txt','w'),stderr=open('latest_err.txt','w'))
        
    def about(self):  # 显示软件信息
        QMessageBox.information(self, "软件信息",
                                "MSL2-Python 22M12R1 \nCode by MojaveHao \nOpenSourced by GNU Affero General Public License v3")
    
    def show_java_path(self):  # 展示默认的Java路径
        if self.cbox_using_java.currentText() == "Java17":
            QMessageBox.information(self, "Java17路径", str(self.java_path[0]))
        if self.cbox_using_java.currentText() == "Java16":
            QMessageBox.information(self, "Java16路径", str(self.java_path[1]))
        if self.cbox_using_java.currentText() == "Java8":
            QMessageBox.information(self, "Java8路径", str(self.java_path[2]))
        if self.cbox_using_java.currentText() == "":
            QMessageBox(self, "提示", "您选择了系统环境变量")
            
    def frp_guide(self, now):  # 调用FRP配置指南
        frpconfig = FRP()
        self.show()
    
    def select_server_path(self):  # 选择服务端路径的函数
        with tqdm(total=6) as pbar:
            pbar.set_description('pyMSL:ResselectingServerPath')
        # self.server_path = QFileDialog.getExistingDirectory(self, "MSL2:选择服务端所在文件夹")  # 选择服务端路径
        self.server_name = QFileDialog.getOpenFileName(self, "MSL2:选择服务端文件",
                                                       filter="Minecraft Java Edi Server File (*.jar)")[0].split(
            '/')  # 选择服务器的Jar文件
        pbar.update(1)
        self.server_path = ''
        pbar.update(1)
        for i in self.server_name[:-1]:
            self.server_path += i + '/'
        pbar.update(1)
        self.server_name = self.server_name[-1]
        pbar.update(1)
        # 把服务端路径设置成默认下载路径
        self.download_path = self.server_path
        pbar.update(1)
        self.lb_path.setText(self.server_path)
        pbar.update(1)
    
    def download_server(self):  # 创建下载窗口
        # download = DManager(self.download_path)
        pass
    
    def visit_help(self):  # 查看帮助
        web.open("https://ntfs2020.github.io/MSL2-Python/#/")
    
    def open_set(self):
        '''显示设置页面'''
        mslsetting = Setting()
        self.show()
        
    def open_logs(self):
        web.open(f"{self.server_path}/logs/latest.log")

    def debug(self,text):
        pass
if __name__ == '__main__':
    app = QApplication(sys.argv)
    msl = MSL2()
    sys.exit(app.exec())

