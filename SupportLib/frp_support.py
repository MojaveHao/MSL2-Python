import os


def sakura_frp_status_setting(now: str):
    if now == "first_use":
        os.system("cd /usr/loacl/bin || wget -O frpc https://getfrp.sh/d/frpc_linux_amd64 ||")
        print("请按照以下步骤操作:\
              \t1.登录natfrp.com并注册账号\n\
              \t2.点击管理面板之后登录,之后先签到获取流量,之后实名认证\n\t以后可以通过每日签到获取免费流量,也可以购买便宜上天的流量包(不是广告)\n\
              \t3.切换到穿透->隧道列表,新建隧道,随便选择一个能用的节点,然后视情况选择协议:\n\tMinecraft Java版选择TCP\n\tMinecraft 基岩版选择UDP\n剩下的按照界面提示填写即可,最后点击确定\n\
              \t4.新建隧道完成,返回首页,点击查看访问密钥之后右键复制,然后在接下来的窗口中黏贴,完成后请顺序摁下Tab+Enter登录")
        os.system("frpc")
        print("接下来请摁方向键选择隧道,摁下空格后高亮即为当前选择(支持多选),选好后摁下Ctrl+C启动,下一次打开会自动启动你的隧道\n\t注意:不能启动两个分别位于不同节点下的隧道")
        print("如果你一步步做下来了,那么你的隧道应该已经成功启动了,恭喜!\n更多请参阅SakuraFRP官方文档:\n\thttps://doc.natfrp.com/#/")
    if now == "after":
        os.system("frpc")


with open("frp.conf", "w") as f:
    f.write("frp configed\nIf you wouldn't to run the guide again,please don't delete this file.")
