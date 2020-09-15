# @Time    : 2020/8/4 22:28
# @Author  : Arvin
# @File    : requests07.py
# @Software: PyCharm
# @Title   : https://studentloanhero.com/marketplace/refinancing/

import requests as rq
import json
if __name__ == '__main__':
    url = 'https://studentloanhero.com/wp-json/slh-product-wizard/v1/products/refinancing'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    }
    data = rq.get(url=url, headers=headers).json()
    fp1 = open('./result/rawData.json', 'w', encoding='utf-8')
    json.dump(data, fp=fp1, ensure_ascii=False)
    company_list = []
    for t in data:
        company = {
            'position': t['position'],
            'name': t['name'],
            'rates': t['rates']['combined'],
            'rates_fixed': t['rates_fixed']['combined'],
            'rates_variable': t['rates_variable']['combined']
        }
        company_list.append(company)
    fp2 = open('./result/processedData.json', 'w', encoding='utf-8')
    json.dump(company_list, fp=fp2, ensure_ascii=False)
    print('over')
