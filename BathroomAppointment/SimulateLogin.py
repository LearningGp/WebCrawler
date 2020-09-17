# @Time    : 2020/9/10 9:41
# @Author  : Arvin
# @File    : SimulateLogin.py
# @Software: PyCharm
# @Title   : 学校系统模拟登录

from selenium import webdriver
from time import sleep
import json
from selenium.common.exceptions import NoSuchElementException
import requests as rq
if __name__ == '__main__':
    bro = webdriver.Chrome(executable_path='./selenium/chromedriver.exe')
    bro.get('http://authserver.nju.edu.cn/authserver/login?service=http%3A%2F%2Fehall.nju.edu.cn%2Flogin%3Fservice%3Dhttp%3A%2F%2Fehall.nju.edu.cn%2Fywtb-portal%2Fofficial%2Findex.html%23%2F')
    userName = bro.find_element_by_id('username')
    passWord = bro.find_element_by_id('password')
    sleep(1)
    userName.send_keys('MF20320057')
    sleep(1)
    passWord.send_keys('3016XmHjh4127')
    sleep(1)
    try:
        captcha = bro.find_element_by_id('captchaResponse')
    except NoSuchElementException as e:
        # 打印异常信息
        print(e)
        # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False

    btn = bro.find_element_by_xpath('//*[@id="casLoginForm"]/p[4]/button')
    btn.click()
    sleep(2)
    bro.get('http://ehallapp.nju.edu.cn/qljfwapp/sys/lwAppointmentBathroom/index.do?t_s=1599708219264&amp_sec_version_=1&gid_=Qm9nNDVML1laR1RkK3FtRGp5cGk5YmwvUHZkWTJ2VUpTUXFUYUpzMnhYMS8yS1g3azQ1dlh0UDdBRGwxOEJWRk5jYkVyL29kVjJUQzU3b0JRSU56d2c9PQ&EMAP_LANG=zh&THEME=magenta#/myAppointment')
    c = bro.get_cookies()
    bro.quit()
    cookies = {}
    for cookie in c:
        cookies[cookie['name']] = cookie['value']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    }
    formData_o = {"USER_ID": "MF20320057",
                  "USER_NAME": "何家欢",
                  "DEPT_CODE": "4270",
                  "DEPT_NAME": "软件学院",
                  "PHONE_NUMBER": None,
                  "PALCE_ID": "f881e8c2aa6f4190bc3efa13408143af",
                  "BEGINNING_DATE": "2020-09-16 19:40",
                  "ENDING_DATE": "2020-09-16 20:00",
                  "SCHOOL_DISTRICT_CODE": "02",
                  "SCHOOL_DISTRICT": "鼓楼校区",
                  "LOCATION": "鼓楼男浴室",
                  "PLACE_NAME": "鼓楼男浴室",
                  "IS_CANCELLED": 0}
    formData = json.dumps(formData_o)
    param = {
        'formData': formData
    }
    url = 'http://ehallapp.nju.edu.cn/qljfwapp/sys/lwAppointmentBathroom/api/appointmentSave.do?'
    response = rq.post(url=url, data=param, headers=headers, cookies=cookies).text
    print(response)