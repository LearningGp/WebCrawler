# @Time    : 2020/9/10 9:20
# @Author  : Arvin
# @File    : SimulateLogin01.py
# @Software: PyCharm
# @Title   : 模拟登录人人网

from VerificationCode import VerificationCode01
from lxml import etree
import requests as rq
if __name__ == '__main__':
    url = 'http://www.renren.com/SysHome.do'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    page_text = rq.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    img_url = tree.xpath('//*[@id="verifyPic_login"]/@src')[0]
    img_data = rq.get(url=img_url, headers=headers).content
    with open('./temp/code.jpg', 'wb') as fp:
        fp.write(img_data)
    chaojiying = VerificationCode01.Chaojiying_Client('lalashadiao', 'Hhklhjh1308', '907861')
    #  用户中心>>软件ID 生成一个替换 96001
    im = open('./temp/code.jpg', 'rb').read()
    #  本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    icode = chaojiying.PostPic(im, 1902)['pic_str']
    print(icode)
    session = rq.Session()
    login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=20208491338'
    data = {
        'email': 'lalashadiao@163.com',
        'icode': icode,
        'origURL': 'http://www.renren.com/home',
        'domain': 'renren.com',
        'key_id': '1',
        'captcha_type': 'web_login',
        'password': '3ceda0d6bf59676debfede5736810dc9625e7d1f3dac8fe247bf1499291b615f',
        'rkey': '17ca0e1068fc1aeb8a61f92cc34ac916',
        'f': 'http%3A%2F%2Fwww.renren.com%2F975093915%2Fnewsfeed%2Fphoto'
    }
    reponse = session.post(url=login_url, headers=headers, data=data)
    print(reponse.status_code)
    print(session.cookies.get_dict())
    detail_url = 'http://www.renren.com/975093915/profile'
    detail_page_text = session.get(url=detail_url, headers=headers).text
    with open('./temp/detail.html', 'w', encoding='utf-8') as fp:
        fp.write(detail_page_text)
