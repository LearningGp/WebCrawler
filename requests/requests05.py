# @Time    : 2020/7/30 10:20
# @Author  : Arvin
# @File    : requests05.py
# @Software: PyCharm
# @Title   : 爬取KFC餐厅地址

import requests as rq
import json
if __name__ == '__main__':
    # 同爬取豆瓣排名
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    pageIndex = 1
    param = {
        'cname': '',
        'pid': '',
        'keyword': '杭州',
        'pageIndex': pageIndex,
        'pageSize': '10',
    }
    # UA伪装：伪装成浏览器正常请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    }
    response = rq.get(url=url, params=param, headers=headers)
    print(response.status_code)
    # 通过返回格式判断需要格式
    list_data = response.json()
    # 获取餐厅总数
    count = list_data['Table'][0]['rowcount']
    pageNum = (count//10)+1
    print("共 %d 个餐厅地址"%(count))
    # 持久化存储
    fp = open('./result/kfc.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)
    # for循环爬取剩下所有餐厅
    for num in range(2, count+1):
        pageIndex = num
        param = {
            'cname': '',
            'pid': '',
            'keyword': '杭州',
            'pageIndex': pageIndex,
            'pageSize': '10',
        }
        response = rq.get(url=url, params=param, headers=headers)
        list_data = response.json()
        fp = open('./result/kfc.json', 'a', encoding='utf-8')
        json.dump(list_data, fp=fp, ensure_ascii=False)
        print(response.status_code)
    print('finished')
