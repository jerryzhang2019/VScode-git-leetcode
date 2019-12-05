# 类方法标记@classmethod,类方法绑定到类上，而不是实例上，类方法的第一个参数将传入类本身，命名为cls.类方法无法获得任何
# 实例变量，只能获得类的引用
# 课堂练习
class Person(object):
    count = 0  # 类属性

    @classmethod
    def how_many(cls):
        return cls.count

    def __init__(self, name):
        self.name = name
        Person.count += 1
print(Person.how_many())
p1 = Person('Bob')
print(Person.how_many())
# 课后作业
class Person(object):
    __count = 0  # 类属性

    @classmethod
    def how_many(cls):
        return cls.__count

    def __init__(self, name):
        self.name = name
        Person.__count += 1
print(Person.how_many())
p1 = Person('Bob')
print(Person.how_many())
