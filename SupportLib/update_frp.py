import time,os
from tkinter import messagebox as mgb
def update():
    time.sleep(5)
    if os.path.isfile("frp.zip"):
        os.system("unzip frp.zip -d /frp/ -o")
        mgb.showinfo("提示","Frp已经更新完成，请重新启动FrpcConfig")