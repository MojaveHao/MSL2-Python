import asyncio
import httpx
import requests

import nest_asyncio
nest_asyncio.apply()

def download(down_url:str,down_name:str,down_path:str,chunk=10):
    def calc_divisional_range(filesize, chuck):
        step = filesize//chuck
        arr = list(range(0, filesize, step))
        result = []
        for i in range(len(arr)-1):
            s_pos, e_pos = arr[i], arr[i+1]-1
            result.append([s_pos, e_pos])
        result[-1][-1] = filesize-1
        return result


    # 下载方法
    async def async_range_download(down_name, s_pos, e_pos):
        headers = {"Range": f"bytes={s_pos}-{e_pos}"}
        res = await client.get(url, headers=headers)
        with open(down_name, "rb+") as f:
            f.seek(s_pos)
            f.write(res.content)

    client = httpx.AsyncClient()

    res = httpx.head(down_url)
    filesize = int(res.headers['Content-Length'])
    divisional_ranges = calc_divisional_range(filesize, 20)


    down_name = down_name
    # 先创建空文件
    with open(f"{down_path}{down_name}", "wb") as f:
        pass

    loop = asyncio.get_event_loop()
    tasks = [async_range_download(down_name, s_pos, e_pos)
            for s_pos, e_pos in divisional_ranges]
    # 等待所有协程执行完毕
    loop.run_until_complete(asyncio.wait(tasks))
