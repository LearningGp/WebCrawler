# @Time    : 2020/8/15 17:34
# @Author  : Arvin
# @File    : xpath03.py
# @Software: PyCharm
# @Title   : 爬取城市名称

import requests as rq
from lxml import etree
if __name__ == '__main__':
    # 分别定位热门城市以及全部城市
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    # }
    # url = 'https://www.aqistudy.cn/historydata/'
    # page_text = rq.get(url=url, headers=headers).text
    #
    # tree = etree.HTML(page_text)
    # hot_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    # all_hotcity_names = []
    # for li in hot_li_list:
    #     hot_city_name = li.xpath('./a/text()')[0]
    #     all_hotcity_names.append(hot_city_name)
    # li_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    # all_city_names = []
    # for li in li_list:
    #     city_name = li.xpath('./a/text()')[0]
    #     all_city_names.append(city_name)
    # print('hotcity:\n', all_hotcity_names, len(all_hotcity_names))
    # print('city:\n', all_city_names, len(all_city_names))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = rq.get(url=url, headers=headers).text

    tree = etree.HTML(page_text)
    #  一次定位热点城市以及所有城市('|'表示或)
    city_a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_names = []
    for city_a in city_a_list:
        city_name = city_a.xpath('./text()')[0]
        all_city_names.append(city_name)
    print(all_city_names)
