# @Time    : 2020/7/28 16:38
# @Author  : Arvin
# @File    : requests04.py
# @Software: PyCharm
# @Title   : 爬取豆瓣电影排名

import requests as rq
import json
if __name__ == '__main__':
    # 同上一案例，虽然可以采用数据分析，但是在此仍采用XHR类型请求
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',  # 起始
        'limit': '20',  # 数量
    }
    # UA伪装：伪装成浏览器正常请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    }
    response = rq.get(url=url, params=param, headers=headers)
    # 通过返回格式判断需要格式
    list_data = response.json()

    # 持久化存储
    fp = open('./douban.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)

    print(response.status_code)
    print('finished')
