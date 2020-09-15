# @Time    : 2020/7/27 10:02
# @Author  : Arvin
# @File    : requests02.py
# @Software: PyCharm
# @Title   : 简易网页采集器

import requests as rq
if __name__ == '__main__':
    # UA伪装：伪装成浏览器正常请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    }
    url = "https://www.baidu.com/s?"
    # 处理url携带的参数：封装到字典中
    kw = input('enter a word:')
    param = {
        'wd': kw
    }
    # 发送携带参数的请求
    response = rq.get(url=url, params=param, headers=headers)

    print(response.status_code)
    page_text = response.text
    fileName = kw+'.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName+'保存成功')
