
from flask import Flask # 如何使用内置函数Flask
from config import DEBUG  # 如何使用自己写的配置文件？
__author__ = 'jerry zhang'

# app = Flask()
app = Flask(__name__)

@app.route('/hello/')  # 装饰器，传入URL路径
def hello():  # 通过HTTp请求访问这个函数
    # 基于类的视图（既插视图）
    return 'Hello, QiYue'

# 如何路由注册？
app.run(host = '0.0.0.0',debug = DEBUG, port = 81)  # 可以被外网访问，端口号也可以用被修改
# app.add_url_rule('/hello', view_func = hello)   # 基于类的视图（既插视图）的情况下使用
# 如何设置自动重启服务器？方法是开启调试模式DEBUG
# app.run(host = '192.168.0.101',debug = True) # 在网页输入如下地址可以代开网页：http://192.168.0.101:5000/hello/缺点是只能固定IP地址访问
# app.run(host = '0.0.0.0',debug = True)  # 可以被外网访问
