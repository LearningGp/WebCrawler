# @Time    : 2020/9/11 8:41
# @Author  : Arvin
# @File    : auto.py
# @Software: PyCharm
# @Title   :

import requests as rq
import json
import execjs
from lxml import etree
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    }
    index_url = 'http://authserver.nju.edu.cn/authserver/login'
    session = rq.Session()
    page_text = rq.get(url=index_url, headers=headers).text
    tree = etree.HTML(page_text)
    lt = tree.xpath('//*[@id="casLoginForm"]/input[1]/@value')[0]
    dllt = tree.xpath('//*[@id="casLoginForm"]/input[2]/@value')[0]
    pwdDefaultEncryptSalt = tree.xpath('//*[@id="pwdDefaultEncryptSalt"]/@value')[0]
    execution = tree.xpath('//*[@id="casLoginForm"]/input[3]/@value')[0]
    eventId = tree.xpath('//*[@id="casLoginForm"]/input[4]/@value')[0]
    rmShown = tree.xpath('//*[@id="casLoginForm"]/input[5]/@value')[0]
    print(lt)
    print(pwdDefaultEncryptSalt)
    print(execution)
    print(eventId)
    print(rmShown)
    file = 'jsCode.js'
    ctx = execjs.compile(open(file, encoding="utf-8").read())
    password = '3016XmHjh4127'
    password = ctx.call("encryptAES", password, pwdDefaultEncryptSalt)
    print(password)

    login_url = 'http://authserver.nju.edu.cn/authserver/login'
    data = {
        'username': 'MF20320057',
        'password': password,
        'lt': lt,
        'dllt': dllt,
        'execution': execution,
        '_eventId': eventId,
        'rmShown': rmShown
    }
    res = session.post(url=login_url, headers=headers, data=data)
    cookie = session.cookies
    for key in cookie.keys():
        print(key, cookie.get(key))
    #  print(res.status_code)
    # print(session.cookies.get_dict())
    # with open('./temp.html', 'w', encoding='utf-8') as fp:
    #     fp.write(res)
    print(res.status_code)



