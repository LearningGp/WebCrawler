# @Time    : 2020/9/16 23:20
# @Author  : Arvin
# @File    : ProxyCrawler01.py
# @Software: PyCharm
# @Title   : 代理爬虫查询IP

import requests as rq
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    }
    url = 'https://www.baidu.com/s?wd=ip'
    page_text = rq.get(url=url, headers=headers, proxies={"https": "220.189.98.6:3000"}).text
    with open('./result2.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
