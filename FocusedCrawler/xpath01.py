# @Time    : 2020/8/12 21:06
# @Author  : Arvin
# @File    : xpath01.py
# @Software: PyCharm
# @Title   : 爬取58二手房中的房源信息

from lxml import etree
import requests as rq
if __name__ == '__main__':
    url = 'https://zhoushan.58.com/ershoufang/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }
    page_text = rq.get(url=url, headers=headers).text

    tree = etree.HTML(page_text)
    # 标签对象列表
    li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
    fp = open('./result/58.txt', 'w', encoding='utf-8')
    for li in li_list:
        # 标签对象再次定位
        title = li.xpath('./div[2]/h2/a/text()')[0]
        print(title)
        fp.write(title+'\n')
