
from http import HTTP

class YuShuBook:

    #定义URL
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    
    # 定义两种查询方法
    @classmethod  # 类方法
    def search_by_isbn(cls,isbn):  # 方法一按照ISBN号查询
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)  # result 是一个字典dict
        return result
        # url = self.isbn_url 另外一种调用url的方法

    @classmethod  # 类方法
    def search_by_keyword(cls,keyword,count=15, start=0 ):  # 方法二按照关键字查询
        url = cls.keyword_url.format(keyword)
        resutl = HTTP.get(url)
        return result
    