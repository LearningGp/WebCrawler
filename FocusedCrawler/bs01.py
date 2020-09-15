# @Time    : 2020/8/7 17:08
# @Author  : Arvin
# @File    : bs01.py
# @Software: PyCharm
# @Title   : 爬取三国演义章节及内容

from bs4 import BeautifulSoup
import requests as rq
if __name__ == '__main__':
    url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    }
    page_text = rq.get(url=url, headers=headers).text

    # 在首页中解析章节标题以及url
    soup = BeautifulSoup(page_text, 'lxml')
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('./result/sanquo.txt', 'w', encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'http://www.shicimingju.com' + li.a['href']
        detail_page_text = rq.get(url=detail_url, headers=headers).text
        # 解析详情页中需要的内容
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        content = div_tag.text
        fp.write(title+':'+content+'\n')
        print(title, 'over')
