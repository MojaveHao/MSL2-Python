from SupportLib.RAM import mem
from SupportLib.cmdl_get_server import get_file_url as gfu
from SupportLib.download import *

min_ram = 1
max_ram = 4
if os.path.isfile('config.txt'):
    with tqdm(total=4, desc='Read config from file') as pbar:
        with open('config.txt') as f:
            temp = f.read()
            pbar.update(1)
            serv_path = temp[0]
            pbar.update(1)
            serv_name = temp[1]
            pbar.update(1)
            log4j2 = temp[2]
            pbar.update(1)
print("\n" * 2)
print("############################################################################################")
print(" \
         __  __ ____  _     ____    ____        _   _              __     __        \n\
         |  \/  / ___|| |   |___ \  |  _ \ _   _| |_| |__   ___  _ _\ \   / /__ _ __ \n\
         | |\/| \___ \| |     __) | | |_) | | | | __| '_ \ / _ \| '_ \ \ / / _ \ '__|\n\
         | |  | |___) | |___ / __/  |  __/| |_| | |_| | | | (_) | | | \ V /  __/ |   \n\
         |_|  |_|____/|_____|_____| |_|    \__, |\__|_| |_|\___/|_| |_|\_/ \___|_|   \n\
                                            |___/                                     ")
while True:
    choice = int(input("############################################################################################\n\
    请选择执行项:\n\
    \t1.设置服务端路径\n\
    \t2.开启服务器\n\
    \t3.内存设置\n\
    \t4.切换Log4j2状态\n\
    \t5.服务器高级设置\n\
    \t6.查看帮助\n\
    \t7.下载Java\n\
    \t8.下载服务端\n\
    \t9.保存当前配置\n\
    \t10.退出\n\
    >>>"))
    if choice == 1:
        serv_path = input("请输入服务端所在路径")
        serv_name = input("请输入服务端名字")
        print("Successful")
        continue
    if choice == 2:
        if serv_path and serv_name and min_ram and max_ram and log4j2:
            os.system(
                "java -Xms{min_ram}G -Xmx{max_ram}G -jar {serv_path}/{serv_name} -Dlog4j2.formatMsgNoLookups=true")
            print("Starting...")
            continue
        if serv_path and serv_name and min_ram and max_ram and log4j2 == False:
            os.system("java -Xms{min_ram}G -Xmx{max_ram}G -jar {serv_path}/{serv_name}")
            print("Starting...")
            continue
    if choice == 3:
        temp = int(input("请选择内存模式:\n1.自动选择\n2.手动选择"))
        if temp == 2:
            min_ram = int(input("请输入最小内存"))
            max_ram = int(input("请输入最大内存"))
            print("Successful")
            continue
        if temp == 1:
            min_ram = 1
            max_ram = mem()[1] * 0.8
            continue
    if choice == 4:
        try:
            log4j2 = bool(input("请输入Log4j2状态"))
            continue
        except:
            print("Error")
            continue
    if choice == 5:
        port = 19132
        pvp = True
        cmdb = False
        motd = "Welcome"
        while True:
            with open(f"{serv_path}/server.properties") as f:
                temp_config = f.read()
            try:
                temp = int(input("请选择您要更改的项：\n\
                                    \t1.服务器端口\n\
                                    \t2.是否开启PVP\n\
                                    \t3.是否开启命令方块\n\
                                    \4.设置服务器选择界面的提示"))
            except:
                if port != None:
                    for i in range(temp_config):  # 遍历server.properties，并且在内存中修改内容
                        if "server-port=" in temp_config[i]:
                            temp_config[i] = "server-port={}".format(port)
                        break
                if pvp != None:
                    for i in range(temp_config):  # 遍历server.properties，并且在内存中修改内容
                        if "pvp=" in temp_config[i]:
                            temp_config[i] = "pvp={}".format(pvp)
                        break
                if cmdb != None:
                    for i in range(temp_config):  # 遍历server.properties，并且在内存中修改内容
                        if "enable-command-block=" in temp_config[i]:
                            temp_config[i] = "enable-command-block={}".format(cmdb)
                if motd != None:
                    for i in range(temp_config):  # 遍历server.properties，并且在内存中修改内容
                        if "motd=" in temp_config[i]:
                            temp_config[i] = "motd={}".format(motd)
                with open(f"{serv_path}" + os.sep + "server.properties", "w") as f:  # 将修改后的内容重新写回server.properties
                    f.write(temp_config)
            if temp == 1:
                try:
                    port = int(input("请输入服务端端口"))
                    if not port:
                        port = 19132
                    print("Successful")
                except:
                    print("Error")
            if temp == 2:
                try:
                    pvp = bool(input("请输入是否开启PVP"))
                    print("Successful")
                except:
                    print("Error")
            if temp == 3:
                try:
                    cmdb = bool(input("请输入是否开启命令方块"))
                    print("Successful")
                except:
                    print("Error")
            if temp == 4:
                motd = input("请输入MOTD")
    if choice == 6:
        try:
            temp = int(input("\t1.如何选择Java/什么是Java\n\t2.如何修改服务器更多配置\n\t3.这是什么"))
        except:
            continue
        if temp == 1:
            print("1.18+ --> Java17\n\
        1.14 - 1.17 --> Java8 - Java16\n\
        1.8 - 1.13 --> Java8\n\
        1.7- --> Java7")
            print("Java是一种编程语言，Minecraft使用Java实现。没有Java,无论是普通Minecraft还是服务器都无法运行.")
        if temp == 2:
            print("请前往您的服务端文件夹，找到server.properites文件，修改内容即可。看不懂的选强请查询Minecraft Wiki.")
        if temp == 3:
            print("这是MSL2-Python的命令行版本.如果您更习惯GUI或者您有4G以上的内存，我们推荐您运行主程序(而不是此程序)来启动GUI.")
            print("软件版本:Pyv1.0.5_cmdl -> Weaheal 2.13")
    if choice == 7:
        os.system("sudo apt update && sudo apt upgrade -y")
        try:
            temp = int(input("你想下载哪个版本的Java?\n\
                \t1.Java17\n\
                \t2.Java16\n\
                \t3.Java8\n\
                \t4.Java7\n"))
        except:
            continue
        if temp == 1:
            os.system("sudo apt install openjdk-17-jdk -y")
        if temp == 2:
            os.system("sudo apt install openjdk-16-jdk -y")
        if temp == 3:
            os.system("sudo apt install openjdk-8-jdk -y")
        if temp == 4:
            os.system("sudo apt install openjdk-7-jre -y")
    if choice == 8:
        print("目前此版本仅支持以下常用服务端:\n\
        \t1.Spigot\n\
        \t2.Mojang\n\
        \t3.Paper\n\
        \t4.Vanilla\n")
        name = input("请输入名字(不要输入序号)")
        ver = input("请输入您想要下载的版本")
        result = gfu(name, ver)
        if result[0] == None:
            print("没有找到资源，请检查您的输入")
            continue
        download(result[0], result[1])
    if choice == 9:
        config = "({serv_path,serv_name,log4j2})"
        with open('config.txt', 'w') as f:
            f.write(config)
    if choice == 10:
        exit()
