# MSL2-Python Development documentation
## File Structure
### Files
####  主程序.py -> MSL2_Python 的主程序
####  frp.conf -> 配置完成SakuraFRP后生成的用于判断的文件(运行后生成)
####  Output.py -> 负责输出界面的后台处理
####  ui_kfq.py -> 负责显示MSL2主程序界面的Python文件
####  ui_output.py -> 负责显示输出界面的Python文件
### Dir
####  Resource -> MSL2_Python调用的图片文件
####  SupportLib -> MSL2_Python调用的支持文件
## 代码结构
### 主程序
####  self.using_java = 0 ->0为17，1为16，2为8
####  self.want_to_download = 0 ->同上
#### self.java_path=["/usr/lib/jvm/java-17-openjdk-amd64","/usr/lib/jvm/java-16-openjdk-amd64","/usr/libjvm/java-8-openjdk-amd64"]
#### self.server_path = "" ->服务端的路径
#### self.min_mem_G = 1 ->最小内存(G)
#### self.max_mem_G = RAM.mem()[1] ->最大内存(G)
#### self.dis_log4j2 = True ->是否禁用log4j2
#### self.online_mode = True ->是否开启正版验证
#### self.max_players = 20 ->最大玩家数量
#### self.serv_port = 19132 ->服务器端口
#### self.pvp = True ->开启PVP
#### self.command_block = True ->开启命令方块
#### self.motd_message = "Welcome!" ->服务器选择界面提示
#### self.select_card = 0 ->打开的选项卡，0为无，1为日志，2为映射，3为关于
#### self.server_status = False ->服务器状态，False为关闭，True为开启
### Defines
#### set_adv -> 向server.properties文件写入配置
#### process_log4j2 -> 处理log4j2的开关
#### how_to_choice -> 提示如何选择Java
#### download_java -> 调用Linux系统命令下载Java
#### start_server -> 开启服务器
#### open_logs -> 调用Output.py以显示日志界面
#### about -> 打印软件信息
#### show_java_path -> 打印当前的Java路径
#### frp_guide -> 调用SupportLib/frp_guide.py来启动SakuraFRP配置向导

##本说明持续更新中
