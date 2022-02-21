import os,random
'''def sakura_frp_status_setting(now:str):
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
        os.system("frpc")'''
def random_str(randomlength=25):
  """
  生成一个指定长度的随机字符串
  """
  random_str = ''
  base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
  length = len(base_str) - 1
  for i in range(randomlength):
    random_str += base_str[random.randint(0, length)]
  return random_str
random_serv_name = random_str()
random_ssh_name = random_str()
random_ssh_port = random.randint(10001,50000)
my_domian = input("请在此输入您的域名(可以到Freenom免费领取,怎么领B站一搜全都是)(必须有一条CNAME或者A记录指向一台有公网IP的主机) :")
common = "[common]\n\
server_addr = frp.freefrp.net\n\
server_port = 19132\n\
token = freefrp.net\n\
\n\
# 穿透需要 Web 访问的内网服务,例如群晖 NAS DSM 的管理界面.\n\
\n"+f"\
[MSL2Py_MCS_http_{random_serv_name}]\n\
type = http\n\
local_ip = 127.0.0.1\n\
local_port = 19132\n\
custom_domains = {my_domian}\n\
subdomain = server\n\
\n\
[mcjes_ssh_{random_ssh_name}]\n\
type = tcp\n\
local_ip = 127.0.0.1\n\
local_port = 22\n\
remote_port = {random_ssh_port}"
os.system("wget -O freefrp.zip https://github.com/fatedier/frp/releases/download/v0.39.1/frp_0.39.1_linux_amd64.tar.gz")
os.system("unzip freefrp.zip")
os.system("tar -xf frp_0.39.1_linux_amd64.tar")
with open("/frp_0.39.1_linux_amd64/FreeFRP/frpc.ini","w") as f:
    f.write(common)