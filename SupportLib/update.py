import time,os
from tkinter import messagebox as mgb
def update():
    time.sleep(5)
    if os.path.isfile("update_pack.zip"):
        os.system("unzip update_pack.zip -o")
        mgb.showinfo("提示","MSL2已经更新完成,请重新启动软件")