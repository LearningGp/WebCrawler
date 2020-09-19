# @Time    : 2020/9/19 16:39
# @Author  : Arvin
# @File    : AsynchronousCrawler02.py
# @Software: PyCharm
# @Title   : 异步协程

import asyncio
import time
import aiohttp

start = time.time()
urls = {
        'http://127.0.0.1:5000/bobo',
        'http://127.0.0.1:5000/jay',
        'http://127.0.0.1:5000/tom'
}


async def get_page(url):
    print('正在下载', url)
    #  使用aiohttp防止同步操作使得异步失效
    async with aiohttp.ClientSession() as session:
        #  记得使用await手动挂起耗时操作
        async with await session.get(url=url) as response:
            page_text = await response.text()
            #  text()返回字符串形式的响应数据
            #  read()返回二进制形式的响应数据
            #  json()返回json形式的响应数据
    print('下载完毕', url, page_text)

tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()

print('总耗时：', end-start)
