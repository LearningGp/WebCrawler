# @Time    : 2020/7/28 16:05
# @Author  : Arvin
# @File    : requests03.py
# @Software: PyCharm
# @Title   : 百度翻译

import requests as rq
import json
if __name__ == '__main__':
    #局部刷新通过ajax实现，在调试中查看XHR类型请求找到携带参数的post请求
    post_url = 'https://fanyi.baidu.com/sug'
    # UA伪装：伪装成浏览器正常请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    }
    # 参数处理
    word = input('enter a word:')
    data = {
        'kw': word
    }
    response = rq.post(url=post_url, data=data, headers=headers)
    # json对象返回obj（需判断响应数据是否为json类型）
    dic_obj = response.json()

    # 持久化存储
    fileName = word+'.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)
    print(response.status_code)
    print('finfished')
