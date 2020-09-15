# @Time    : 2020/9/4 16:44
# @Author  : Arvin
# @File    : xpath04.py
# @Software: PyCharm
# @Title   : 爬取简历模板

import requests as rq
from lxml import etree
if __name__ == '__main__':
    page_number = int(input('Enter the number of pages required:'))
    url = 'http://sc.chinaz.com/jianli/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }
    for page in range(1, page_number+1):
        if page != 1:
            url_page = url+'free_'+str(page)+'.html'
        else:
            url_page = url+'free.html'
        page_text = rq.get(url=url_page, headers=headers).text
        page_tree = etree.HTML(page_text)
        # 获取简历模板详情页url列表
        list_page_urls = page_tree.xpath('//div[@id="container"]/div/a')
        # 循环请求每个详情页
        for list_page_url in list_page_urls:
            page_url = list_page_url.xpath('./@href')[0]
            page_name = list_page_url.xpath('./img/@alt')[0]
            page_name = page_name.encode('iso-8859-1').decode('utf-8')
            detail_page_text = rq.get(url=page_url, headers=headers).text
            detail_tree = etree.HTML(detail_page_text)
            download_url = detail_tree.xpath('//*[@id="down"]/div[2]/ul/li[12]/a/@href')[0]
            download_data = rq.get(url=download_url, headers=headers).content
            download_path = './result/jianli/' + page_name + '.rar'
            with open(download_path, 'wb') as fp:
                fp.write(download_data)
                print(page_name+'over')
