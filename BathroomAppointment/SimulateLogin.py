# @Time    : 2020/9/10 9:41
# @Author  : Arvin
# @File    : SimulateLogin.py
# @Software: PyCharm
# @Title   : 学校系统模拟登录

from selenium import webdriver
from time import sleep
import json
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import requests as rq
if __name__ == '__main__':
    #  参数
    myUsername = ''
    myPassword = ''
    myName = ''
    beginTime = '2020-10-15 21:40'
    endTime = '2020-10-15 22:00'
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gup')
    bro = webdriver.Chrome(executable_path='./selenium/chromedriver.exe', chrome_options=chrome_options)
    bro.get('')
    #  教务系统登录url
    userName = bro.find_element_by_id('username')
    passWord = bro.find_element_by_id('password')
    sleep(1)
    userName.send_keys(myUsername)
    sleep(1)
    passWord.send_keys(myPassword)
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
    bro.get('')
    #  浴池预约url
    c = bro.get_cookies()
    bro.quit()
    cookies = {}
    for cookie in c:
        cookies[cookie['name']] = cookie['value']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    }
    #  补全对应信息
    formData_o = {"USER_ID": myUsername,
                  "USER_NAME": myName,
                  "DEPT_CODE": "",
                  "DEPT_NAME": "",
                  "PHONE_NUMBER": None,
                  "PALCE_ID": "f881e8c2aa6f4190bc3efa13408143af",
                  "BEGINNING_DATE": beginTime,
                  "ENDING_DATE": endTime,
                  "SCHOOL_DISTRICT_CODE": "02",
                  "SCHOOL_DISTRICT": "",
                  "LOCATION": "",
                  "PLACE_NAME": "",
                  "IS_CANCELLED": 0}
    formData = json.dumps(formData_o)
    param = {
        'formData': formData
    }
    url = 'http://ehallapp.nju.edu.cn/qljfwapp/sys/lwAppointmentBathroom/api/appointmentSave.do?'
    response = rq.post(url=url, data=param, headers=headers, cookies=cookies).text
    print(response)

    # 规避检测
    # from selenium.webdriver import Chrome
    # from selenium.webdriver import ChromeOptions
    #
    # option = ChromeOptions()
    # option.add_experimental_option('excludeSwitches', ['enable-automation'])
    # driver = Chrome(options=option)
