# MSL2-Python Development documentation

## File Structure

### Files

- 主程序.py -> MSL2-Python 的主程序

- frp.conf -> 配置完成SakuraFRP后生成的用于判断的文件(运行后生成)

- Output.py -> 负责输出界面的后台处理，包括读取日志文件

- ui_kfq.py -> 负责显示MSL2主程序界面的Python文件

- ui_output.py -> 负责显示输出界面的Python文件

- download_server_support.py -> 负责服务端下载页面的处理

### Dir

- Resource -> MSL2-Python调用的图片文件

- SupportLib -> MSL2-Python调用的支持文件

    - __init__.py -> 让主程序能够调用同级目录下文

    - download.py -> 多线程下载器,由Bilibili @2z0h0m9 制作,用于下载服务端

    - frp_support.py -> 内网穿透教实现程序(实验中)

    - RAM.py -> 计算并返回当前总内存与可用内存

    - cmdl_get_server-> 获取服务端下载路径（感谢[Sakura's Mirror](mirror.zerodream.net)提供的镜像服务)

    - ui_download.py -> 负责显示服务端下载页面

- MSLDownload -> MSL2-Python的默认下载路径(运行后生成)

## 代码结构

### 主程序

- self.using_java = 0 ->0为17,1为16,2为8

- self.want_to_download = 0 ->同上

-

self.java_path=["/usr/lib/jvm/java-17-openjdk-amd64","/usr/lib/jvm/java-16-openjdk-amd64","/usr/libjvm/java-8-openjdk-amd64"]
-> 第一个为Java17路径，第二个为Java16路径，第三个为Java8路径，默认为Ubuntu系统

- self.server_path = "" ->服务端的路径,默认为空,即当前目录

- self.min_mem_G = 1 ->最小内存(G)

- self.max_mem_G = RAM.mem()[1] ->最大内存(G)

- self.dis_log4j2 = True ->是否禁用log4j2

- self.online_mode = True ->是否开启正版验证

- self.max_players = 20 ->最大玩家数量

- self.serv_port = 19132 ->服务器端口

- self.pvp = True ->开启PVP

- self.command_block = True ->开启命令方块

- self.motd_message = "Welcome!" ->服务器选择界面提示

- self.select_card = 0 ->打开的选项卡,0为无,1为日志,2为映射,3为关于

- self.server_status = False ->服务器状态,False为关闭,True为开启

### Output.py [已弃用]

- self.server_path -> 读取(f"{self.server_path}"+os.sep+"server.log")文件[已弃用]

## Defines

### 主程序

- set_adv -> 向server.properties文件写入配置

- process_log4j2 -> 处理log4j2的开关

- how_to_choice -> 提示如何选择Java

- download_java -> 调用Linux系统命令下载Java

- start_server -> 开启服务器

- open_logs -> 调用Output.py以显示日志界面

- about -> 打印软件信息

- show_java_path -> 打印当前的Java路径

- frp_guide -> 调用SupportLib/frp_guide.py来启动内网穿透配置向导

### Output.py [已弃用]

- readlog -> 反复读取(f"{self.server_path}"+os.sep+"server.log")文件[已弃用]
- 此文件已经弃用，将在未来删除。相关功能已经转移到主程序。