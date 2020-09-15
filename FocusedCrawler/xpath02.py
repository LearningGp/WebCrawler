# @Time    : 2020/8/13 10:14
# @Author  : Arvin
# @File    : xpath02.py
# @Software: PyCharm
# @Title   : 爬取图片

import requests as rq
from lxml import etree
if __name__ == '__main__':
    page_number = int(input('Enter the number of pages required:'))
    url = 'http://pic.netbian.com/4kdongman/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }
    for page in range(1, page_number+1):
        if page != 1:
            url_page = url+'index_'+str(page)+'.html'
        else:
            url_page = url+'index.html'
        page_text = rq.get(url=url_page, headers=headers).text
        page_tree = etree.HTML(page_text)
        # 获取图片详情页url列表
        list_page_url = page_tree.xpath('//*[@id="main"]/div[3]/ul/li/a/@href')
        # 循环请求每个详情页
        for page_url in list_page_url:
            url_page_detail = 'http://pic.netbian.com'+page_url
            page_detail_text = rq.get(url=url_page_detail, headers=headers).text
            page_detail_tree = etree.HTML(page_detail_text)
            img_url = page_detail_tree.xpath('//*[@id="img"]/img/@src')[0]
            img_name = page_detail_tree.xpath('//*[@id="img"]/img/@title')[0]
            img_name = img_name.encode('iso-8859-1').decode('gbk')
            img_url = 'http://pic.netbian.com'+img_url
            img_path = './result/imgs/'+img_name+'.jpg'
            img_data = rq.get(url=img_url, headers=headers).content
            with open(img_path, 'wb') as fp:
                fp.write(img_data)
                print(img_name+' over')
