# Welcome to the MSL2-Python wiki!
## 使用前
- 下载运行环境
	- Python
		- 本版本开服器使用Python编写，由于使用库的限制，请务必更新至Python3.7以上
			- 现在请您先输入python -ver查看现存Python版本，3.6以下都不可以运行
			- 如果您是Python2.x：请在终端输入sudo apt-get remove --auto-remove python2.x  来移除Python(把x换成后面的版本号)
			- 如果您是Python3.x：
				- Python3.7以上可以直接跳到下载PySide6一节
				- Python3.7以下可以查看[教程](https://cloud.tencent.com/developer/article/1565853)或自己折腾
	- 下载PySide6和其他运行环境
	 	- 如果您已经配置好了Python3.7环境，请在终端执行sudo pip3 install PySide6来下载PySide6运行环境
	 		- 其他环境安装：将以下库名替换到上面一条命令PySide6的位置
                - tqdm
                - requests
                - multitasking
                - signal
                - retry
                - urllib
                - psutil
	       至此环境配置已经完成
## 基本使用方法
- 开启服务器
	- 在主界面点击“开启服务器”即可
	- 注意事项
		- 必须事先选择服务端路径和服务端（服务端没有可以点击服务端路径和“...”选择路径中间的下载摁钮下载）
		- 必须配置好对应版本的Java,不知道如何配置可以点击主页下方的“如何选择”查看帮助
- 配置服务器
	- 主页提供了常用的服务器设置，如是否开启PVP，最大在线人数等
	- 进阶设置可以在服务端路径下的server.properties修改，具体每个选项的释义可以在主界面-帮助 查看
	- 服务端目录结构，开服前准备都可以在主界面-帮助查看

