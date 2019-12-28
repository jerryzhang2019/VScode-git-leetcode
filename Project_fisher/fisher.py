__author__ = 'jerry zhang'

from flask import Flask,make_response # 如何使用内置函数Flask
from helper import  is_isbn_or_key  # 从helper中导入处理关键字和isbn的函数
# from config import DEBUG  # 如何使用自己写的配置文件？


# app = Flask()
app = Flask(__name__)
app.config.from_object('config')  # 如何导入配置文件？括号内接收模块的路径
# print(app.config['DEBUG'])  # 返回结果为True

# 项目的第一个视图函数
@app.route('/book/search/<q>/<page>')
def search(q, page):  # 关键字搜索和ISBN搜索
    """
    q start count isbn 四种关键字简化为q: 普通关键字 isbn 和 page
    """
# 以下代码是用来判断q是isbn还是关键字
# 如何调用API?
    # isbn isbn13 13个0到9的数字组成
    # isbn10 10个0到9数字组成，含有一些’-‘

    isbn_or_key = is_isbn_or_key(q)  # 子函数调用 函数被封装在helper中

'''
@app.route('/hello/')  # 装饰器，传入URL路径
def hello():  # 通过HTTp请求访问这个函数 叫做视图函数
    # 基于类的视图（既插视图）
    # status code 200,404,301
    # content - type http headers
    # content - type = text/html
    # response
    headers = {
        # 'content-type': 'text/plain',
        'content-type': 'application/json',
        'location': 'http://www.bing.com'  # 重定向 如果寻找的地址不存在，则重新跳转到新的网址
    }
    # response = make_response('<html></html>', 404)  # 创建response对象
    """
    response = make_response('<html></html>', 301)  # 创建response对象
    response.headers = headers
    return response
   """
    # 使用下面一行替换上面3行代码
    return '<html></html>', 301, headers

    # return '<html></html>'
    # return 'Hello, QiYue'
'''
if __name__ == '__main__': # 入口文件
    # 生产环境 nginx + uwsgi
    # 如何路由注册？字典 dict 子类
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)  # 可以被外网访问，端口号也可以用被修改

# app.run(host = '0.0.0.0',debug = DEBUG, port = 81)  # 可以被外网访问，端口号也可以用被修改,其中一个方法和import config 配合使用
# app.add_url_rule('/hello', view_func = hello)   # 基于类的视图（既插视图）的情况下使用
# 如何设置自动重启服务器？方法是开启调试模式DEBUG
# app.run(host = '192.168.0.101',debug = True) # 在网页输入如下地址可以代开网页：http://192.168.0.101:5000/hello/缺点是只能固定IP地址访问
# app.run(host = '0.0.0.0',debug = True)  # 可以被外网访问
