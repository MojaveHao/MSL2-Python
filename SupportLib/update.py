import os
import time


def update():
    time.sleep(5)
    if os.path.isfile("update_pack.zip"):
        os.system("unzip update_pack.zip -o")
        print("MSL2 Updated Successful")
