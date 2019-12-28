
# urllib
# requests

from urllib import request
import requests
class HTTP:  # 两种方法没有区别
# class HTTP(object):
    @staticmethod  # 装饰器 静态方法
    # def get(self, url, return_json = True): 由于是静态方法，括号内不需要加入self
    def get(url, return_json=True):
        r = requests.get(url)
        # restful
        # json
        '''
        if r.status_code == 200:
            if return_json:
                return r.json()  # 返回json格式
            else:
                return r.text  # 返回普通文本格式
        else:
            if return_json:
                return {}
            else:
                return ''
         '''
        # 把上面的代码简化为以下3行代码，利用三元表达式。三元表达式在另外的课程有解释
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
