# @Time    : 2020/8/3 9:21
# @Author  : Arvin
# @File    : requests06.py
# @Software: PyCharm
# @Title   : 爬取国家药品监督管理局

import requests as rq
import json
if __name__ == '__main__':
    # 分析得详情页url为固定url+id值，而id值可以从首页ajax请求到的json串中获取
    url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    }
    id_list = []  # 存储id
    all_data_list = []  # 存储结果
    # 获取id
    for page in range(1, 6):  # 页码范围
        page = str(page)
        data = {
            "on": "true",
            "page": page,
            "pageSize": "15",
            "productName": "",
            "conditionType": "1",
            "applyname": "",
            "applysn": "",
        }
        json_ids = rq.post(url=url, headers=headers, data=data).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
    # print(id_list)
    for detail_id in id_list:
        detail_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
        detail_data = {
            "id": detail_id,
        }
        detail_json = rq.post(url=detail_url, headers=headers, data=detail_data).json()
        # print(detail_json)
        all_data_list.append(detail_json)
    fp = open('./result/allData.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False)
    print('finished')

