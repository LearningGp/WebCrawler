# @Time    : 2020/7/26 17:18
# @Author  : Arvin
# @File    : requests01.py
# @Software: PyCharm
# @Title   : 爬取百度首页

import requests as rq
if __name__ == '__main__':
    # step1：指定url
    url = "https://www.baidu.com/"
    # step2：发起请求
    response = rq.get(url=url)
    # step3：获取响应数据
    page_text = response.text
    print(response.status_code)
    # step4：持久化存储
    with open('./baidu.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print("finished")
