# @Time    : 2020/9/17 15:17
# @Author  : Arvin
# @File    : AsynchronousCrawler01.py
# @Software: PyCharm
# @Title   : 爬取梨视频的视频数据

import requests as rq
from lxml import etree
import random

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    }
    session = rq.Session()
    index_url = 'https://www.pearvideo.com/category_5'
    index_page_text = session.get(url=index_url, headers=headers).text
    tree = etree.HTML(index_page_text)
    li_list = tree.xpath('//*[@id="listvideoListUl"]/li')

    for li in li_list:
        detail_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
        name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
        detail_text = session.get(url=detail_url, headers=headers).text
        data = {
            'contId': '1697449',
            'mrd': random.random()
        }
        url = 'https://www.pearvideo.com/videoStatus.jsp'
        re = session.get(url=url, headers=headers, data=data)
        print(re.text)
        # print(detail_url, name)
        # detail_tree = etree.HTML(detail_text)

