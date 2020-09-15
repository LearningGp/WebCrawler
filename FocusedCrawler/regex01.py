# @Time    : 2020/8/5 22:25
# @Author  : Arvin
# @File    : regex01.py
# @Software: PyCharm
# @Title   : 糗事百科糗图中所有图片（正则）

import requests as rq
import re
import os
if __name__ == '__main__':
    # 创建文件夹保存图片
    if not os.path.exists('./result/qiutuLibs'):
        os.mkdir('./result/qiutuLibs')
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    }
    # 循环请求
    for pageNum in range(1, 3):
        new_url = format(url % pageNum)

        page_text = rq.get(url=new_url, headers=headers).text

        # 使用聚焦爬虫解析数据
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        # print(page_text)
        img_src_list = re.findall(ex, page_text, re.S)
        # print(img_src_list)
        for src in img_src_list:
            src = 'https:' + src
            img_data = rq.get(url=src, headers=headers).content
            # 生成图片名称
            img_name = src.split('/')[-1]
            imgPath = './result/qiutuLibs/'+img_name
            with open(imgPath, 'wb') as fp:
                fp.write(img_data)
                print(img_name, 'finished')
    print('over')
