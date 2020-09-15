# @Time    : 2020/9/9 16:50
# @Author  : Arvin
# @File    : VerificationCode02.py
# @Software: PyCharm
# @Title   : 识别古诗文验证码

from VerificationCode import VerificationCode01
from lxml import etree
import requests as rq
if __name__ == '__main__':
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    page_text = rq.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    img_url = 'https://so.gushiwen.cn' + tree.xpath('//*[@id="imgCode"]/@src')[0]
    img_data = rq.get(url=img_url, headers=headers).content
    with open('./result/code.jpg', 'wb') as fp:
        fp.write(img_data)
    chaojiying = VerificationCode01.Chaojiying_Client('lalashadiao', 'Hhklhjh1308', '907861')
    #  用户中心>>软件ID 生成一个替换 96001
    im = open('./result/code.jpg', 'rb').read()
    #  本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    print(chaojiying.PostPic(im, 1902))