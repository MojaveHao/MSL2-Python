# 使用前

## 下載運行環境

### Python
- Linux(命令行安裝，請準備好sudo權限)
現在請您先輸入python -ver查看現存Python版本，3.6以下都不可以運行

- 如果您是Python2.x，請在終端輸入sudo apt remove --auto-remove python2.x 來移除Python(把x換成後面的版本號)，然後按照Python3.x-Python3.7以下處理

- 如果您是Python3.x：

    - Python3.7以上可以直接跳到下載PySide6一節

    - Python3.7以下可以查看[教程](https://cloud.tencent.com/developer/article/1565853)或自己折騰
	
	- Windows/macOS(官網直接下載安裝包安裝)
		- Windows前往[Python官網](https://www.python.org/downloads/windows/)
		- macOS前往[Python官網](https://www.python.org/downloads/macos/)
		- Windows用戶下載Windows installer(64-bit)
		- macOS用戶下載macOS 64-bit universal2 installer
    
    - Arch特編
	    - 首先恭喜您選擇了Arch Linux！（沒收廣告費啊）
    
	    - 由於最新版本的Arch Linux已經停止了Python3.7以前版本的支持，本文不做說明
    
        -  事實上，您只需要運行以下命令，這會安裝Python3.10.4：
	    ```pacman -S python```
	
		 - 如果您希望使用Python311，請您使用AUR：
			- [Python311 on AUR](https://aur.archlinux.org/packages/python311)
	
			- [AUR]([Arch User Repository - ArchWiki (archlinux.org)](https://wiki.archlinux.org/title/Arch_User_Repository))
	
			- [Pacman]([pacman - Arch Linux 中文維基 (archlinuxcn.org)](https://wiki.archlinuxcn.org/wiki/Pacman))
	
			- 作為一個老練的Arch Linux用戶，您應該知道怎麽使用
			
			- 對於純萌新，我們向您介紹yay
				- 安裝
					- 以root賬戶執行下列命令：
					```
					pacman -S git go base-devel
					git clone https://aur.archlinux.org/yay.git
					cd yay
					makepkg -si
					```
					
				- 使用
				
					- 它的語法和pacman一致。
					- 示例：您可以通過以下語句來安裝Python3.11:
						```yay -s python311```



### PySide6和其他運行環境

- 如果您已經配置好了Python3.7(或更高)環境，請在終端執行.\update_requirements以安裝依賴

	- 註：此處請保證終端的路徑處於我們的項目文件根目錄

	- 註2：如果您正在使用Linux請將pip替換為sudo pip3

### Java
- 雖然開服器本身並不需要Java，可Java是開服的必需品，所以在此一並列出其下載方式（僅針對Linux）
	- 如您的發行版可以使用apt，請按照您的情況選擇命令（必須要有root權限，推薦直接復製）：
		- 首先，更新您的下載源：sudo apt update && sudo apt upgrade -y
		- Java17：sudo apt install openjdk-17-jdk -y
		- Java16：sudo apt install openjdk-16-jdk -y
		- Java8：sudo apt install openjdk-8-jdk -y
		- Java7：sudo apt install openjdk-7-jdk -y
	- 如果您的發行版使用不了apt或者上面的命令報錯，請嘗試下面的方法：
		- [Java17下載](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html)
		- [Java16下載](https://www.oracle.com/java/technologies/javase/jdk16-archive-downloads.html)
		- [Java8下載](https://www.oracle.com/java/technologies/javase/javase8u211-later-archive-downloads.html)
		- [Java7下載](https://www.oracle.com/java/technologies/javase/javase7-archive-downloads.html)
		- [Deepin安裝Java17示例](https://bbs.deepin.org/post/236160)
	- Arch特編
		-  OpenJDK
			-  JDK18(jdk18-openjdk)[AUR](https://aur.archlinux.org/packages/jdk18-openjdk)
			-  JDK16(jdk16-openjdk)[AUR](https://aur.archlinux.org/packages/jdk16-openjdk)
			-  JDK8(jdk8-openjdk-shenandoah)[AUR](https://aur.archlinux.org/packages/jdk8-openjdk-shenandoah)
			-  非常抱歉，JDK17資料暫缺，如有讀者發現可以提交PR
		- 使用方法
			- 大佬請自便
			- 萌新可使用```yay -s (JDK名字後面的括號裏的內容，不要帶上括號)```來安裝對應版本

環境配置至此完成

# 基本使用方法

- 開啟服務器
    - 在主界面點擊「開啟服務器」即可
    - 註意事項
        - 必須事先選擇服務端路徑和服務端（服務端沒有可以點擊服務端路徑和「...」選擇路徑中間的下載摁鈕下載）
        - 必須配置好對應版本的Java,不知道如何配置可以點擊主頁下方的「如何選擇」查看幫助
- 配置服務器
    - 主頁提供了常用的服務器設置，如是否開啟PVP，最大在線人數等
    - 進階設置可以在服務端路徑下的server.properties修改，每個選項的釋義可以在[這裏](#server.properties中部分常用配置翻譯)查看
    - 服務端目錄結構，開服前準備都可以在主界面-幫助查看

# 進階設置和疑難解答

- 更改Java的安裝路徑：見主程序第23行

- 你的系統用不了apt/apt庫裏沒有Java16，17，只有8和11：請自行下載deb包安裝（一般情況下帶GUI的系統可以直接雙擊安裝），然後在上面的「更改Java路徑」解決辦法手動指定Java安裝路徑
    - [Java17](https://www.oracle.com/java/technologies/downloads/)

    - [Java16](https://www.oracle.com/java/technologies/javase/jdk16-archive-downloads.html)

    - [Java8](https://www.oracle.com/java/technologies/javase/javase8u211-later-archive-downloads.html)

    - [命令行安裝教程](https://blog.csdn.net/oMcLin/article/details/108725325)

    - 倉庫相關
        - 服務器相關問題請自行Bing，不是MSL2的問題不要在倉庫提交issues（除非你有好的建議）
        - 參與討論可以提交issues
        - 改好了請直接提交PR，詳細描述解決的是什麽問題，咋解決的

          ### 使用自定義域名

			您得先有一個域名，然後參照以下教程：
            - [阿裏雲](https://doc.natfrp.com/#/app/mc?id=srv-aliyun)

            - [騰訊雲](https://doc.natfrp.com/#/app/mc?id=srv-tencent)

            - [CloudFlare](https://doc.natfrp.com/#/app/mc?id=srv-cloudflare)

### 常用指令

- /ban <玩家名/玩家IP地址>  封禁玩家名/玩家IP地址
	
- /tick <玩家名/玩家IP地址>  臨時踢出玩家名/玩家IP地址

### server.properties中部分常用配置翻譯

    	```
    	 [int]代表一個整數
    	
    	 [str]代表一串字符
    	
    	 [True/False]代表您只能選擇True(是)或者Flase(否)作為值
    	```

- spawn-protection 通過將該值進行 2x+1
的運算來決定出生點的保護半徑，設置為0將只保護出生點下方那一個方塊。[int]
- max-tick-time 設置每個tick花費的最大毫秒數，超時會報錯」Can't keep up!「[int]
- query.port 服務器的端口號[int]
- generator-settings 用於自定義超平坦世界的生成[str]
- sync-chunk-writes 為true時區塊文件以同步模式寫入(跟本地一樣加載) [True/False]
- force-gamemode 強製玩家加入時為默認遊戲模式[True/False]
- allow-nether 是否允許下界[True/False]
- enforce-whitelist 在服務器上強製使用白名單[True/False]
- gamemode 默認遊戲模式 [0生存 1創造 2冒險 3旁觀]
- player-idle-timeout 允許的掛機時間，單位為分鐘，超過後自動踢出[int]
- difficulty 世界難度  [0和平 1簡單 2普通 3困難]
- spawn-monsters 生成攻擊型生物（怪物）[True/False]
- op-permission-level OP權限等級[int]
- pvp 是否允許玩家互相攻擊[True/False]
- entity-broadcast-range-percentage 實體渲染範圍百分比[int]
- level-type 地圖的生成類型[str]
- hardcore 極限模式（死後自動封禁）[True/False]
- enable-command-block 啟用命令方塊[True/False]
- max-players 服務器最大玩家數限製[int]
- network-compression-threshold 網絡壓縮閾值[int]
- -1 代表禁用壓縮
- 0 代表全部壓縮
- 數字越大越節省帶寬，但同時也會加重CPU負擔
- max-world-size 最大世界大小[int]
- function-permission-level 設定函數的默認權限等級[int]
- server-port 服務器端口[int]
- server-ip 服務器ip，若不綁定請留空[int]
- spawn-npcs 是否生成村民和其他NPC[True/False]
- allow-flight 是否允許玩家飛行[True/False]
- level-name 地圖名稱，不要使用中文[str]
- view-distance 服務器發送給客戶端的數據量，決定玩家能設置的視野[int]
- resource-pack 統一資源標識符 (URI) 指向一個資源包。玩家可選擇是否使用[str]
- spawn-animals 是否生成動物[True/False]
- white-list 是否開啟白名單[True/False]
- generate-structures 生成世界時生成結構（如村莊）禁止後地牢和地下要塞仍然生成[True/False]
- online-mode Minecraft在線（正版）驗證[True/False]
- max-build-height 玩家在服務器放置方塊的最高高度[True/False]
- level-seed 地圖種子[int/str]
- prevent-proxy-connections 是否允許玩家使用網絡代理進入服務器[True/False]
- use-native-transport 是否使用針對Linux平臺的數據包收發優化 (僅Linux)[True/False]
- motd 服務器信息展示 （MOTD）[str]
- 更多詳見[Minecraft Wiki](https://minecraft.fandom.com/zh/wiki/Server.properties?variant=zh)

### 使用Nginx進行反向代理

- 什麽是Nginx

	- Nginx (讀作"engine X") 由Igor Sysoev(俄羅斯)於2005年編寫，是一個免費、開源、高性能的HTTP服務器和反向代理，也可以作為一個IMAP/POP3代理服務器。Nginx因為穩定，豐富的功能集，配置簡單，資源占用低而聞名世界。

# 關於

[![OSCS Status](https://www.oscs1024.com/platform/badge/NTFS2020/MSL2-Python.svg?size=large)](https://www.murphysec.com/dr/AT6tw4TErqgElQ4mxs)

MSL2-Python(pyMSL)
Code by MojaveHao/Mojavium

Copyright MojaveHao and David2022 and contributors 2022.

Thanks:

- David2022/Xian66 --- Fixed bugs and supplied MOS II(Download Source) 
  

Open Source License:GNU Affero Genral Public License v3([View at there](https://www.gnu.org/licenses/agpl-3.0.en.html))

## More

Discourages and does not support all commercial use
Without permission, no one may use images and icons, or the original text of the introduction about the origin of the name MSL2-Python at the beginning of this article, for commercial purposes or on the homepage of the project, or other unauthorized acts.

Derivative software needs to declare reference
If the MSL2-Python distribution package is referenced without modifying it, the derived project should mention the use of MSL2-Python anywhere in the description.
If the MSL2-Python source code is modified and republished, or another project is published with reference to the internal implementation of MSL2-Python, the derivative project must be clearly declared from this repository at the beginning of the article or where the 'MSL2-Python' related content first appears (https: //github.com/NTFS2020/MSL2-Python). The fact that it is free and open source must not be distorted or hidden.

# 快捷工具

- 快速更新GUI
	使用update_gui.cmd(Windows)或.\update_gui(Linux)來快速更新已有的.ui文件，請自行添加您添加的其他的.ui文件 
- 快速更新需求庫
	使用update_requirements.cmd(Windows)或.\update_requirements(Linux)來快速更新MSL2-Python所需的庫文件