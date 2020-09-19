# @Time    : 2020/9/19 16:59
# @Author  : Arvin
# @File    : flaskTest.py
# @Software: PyCharm
# @Title   :

from flask import Flask
import time

app = Flask(__name__)

@app.route('/bobo')
def index_bobo():
    time.sleep(2)
    return 'Hello bobo'

@app.route('/jay')
def index_jay():
    time.sleep(2)
    return 'Hello jay'

@app.route('/tom')
def index_tom():
    return 'Hello tom'


if __name__ == '__main__':
    app.run(threaded=True)
