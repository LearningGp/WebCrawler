# @Time    : 2020/9/9 7:43
# @Author  : Arvin
# @File    : BathroomAppointment.py
# @Software: PyCharm
# @Title   : 浴池预约，模拟登录暂时不能使用，采用手动cookie

import requests as rq
import json
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        'Cookie': 'EMAP_LANG=zh; THEME=magenta; _WEU=N6A1kHsxFDxhkqGfqLVkQ0PsdehPnadiL7ti8zKdBknnd7fAhCyyuah5is9RSScLmD_nupOdSf1YrINzHgN51oEsxzxoSWu12EnwPj3mOgZt6Z45VguVZ3Vabdea1NMlahfDVZqGp52RkmBqxnvFmj..; _ga=GA1.3.342546799.1599477930; iPlanetDirectoryPro=xpma5sQJJx56MZvyqvkYbZ; MOD_AUTH_CAS=MOD_AUTH_ST-1206644-LFFHft32qtKQitpJmpBf1599699455126-fQpY-cas; JSESSIONID=USJ1grb4NX8EoIh_rGb8F89XJthclA30qJTN9GiUXwOG3EpEr9GP!396265732; zg_did=%7B%22did%22%3A%20%22174670d54463c9-0df8ef383501bd-f7b1332-144000-174670d5447466%22%7D; zg_=%7B%22sid%22%3A%201599699456177%2C%22updated%22%3A%201599699456185%2C%22info%22%3A%201599456760913%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22ehall.nju.edu.cn%22%2C%22cuid%22%3A%20%22MF20320057%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201599699456177%7D'
    }
    # session = rq.Session()
    # login_url = 'http://authserver.nju.edu.cn/authserver/login?service=http%3A%2F%2Fehall.nju.edu.cn%2Flogin%3Fservice%3Dhttp%3A%2F%2Fehall.nju.edu.cn%2Fywtb-portal%2Fofficial%2Findex.html'
    # data = {
    #     'username': 'MF20320057',
    #     'password': 'QFM0FVdYycx5EE7DzFcyf+Vf9BUJym59lEBnFA0U5hwVnX1y955I0F7a7Y46fcT+NbzJPA+8ODA7843e1zOl8Ll1kBrAtBhoB30tuKfows0=',
    #     'lt': 'LT-728877-TR665rkZKeelEonz2hU3dufaoa3AyE1599607467338-HBn5-cas',
    #     'dllt': 'userNamePasswordLogin',
    #     'execution': 'e1s1',
    #     '_eventId': 'submit',
    #     'rmShown': '1'
    # }
    # response_login = session.post(url=login_url, headers=headers, data=data)
    # print(response_login.status_code)
    # print(response_login.cookies.get_dict())
    formData_o = {"USER_ID": "MF20320057",
                     "USER_NAME": "何家欢",
                     "DEPT_CODE": "4270",
                     "DEPT_NAME": "软件学院",
                     "PHONE_NUMBER": None,
                     "PALCE_ID": "f881e8c2aa6f4190bc3efa13408143af",
                     "BEGINNING_DATE": "2020-09-10 19:00",
                     "ENDING_DATE": "2020-09-10 19:20",
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
    response = rq.post(url=url, data=param, headers=headers).text
    print(response)
