# 访问限制即是建立私有属性：如果一个属性由双下划线开头(__)，该属性就无法被外部访问
class Person(object):
    def __init__(self, name):
        self.name = name
        self._title = 'Mr'
        self.__job = 'Student'  # 双下划线是私有属性
p = Person('Bob')
print(p.name)
print(p._title)
# print(p.__job)  # __job是私有属性 不能被外部打印

