#Create by 2z0h0m9(由NTFS2020上传)
import psutil


def mem():
    data = psutil.virtual_memory()
    total = data.total  # 总内存,单位为byte
    free = data.available  # 可用内存
    memory = "%d" % (int(round(data.percent))) + "%" + " "  # 内存使用情况
    return (total,free,memory)
