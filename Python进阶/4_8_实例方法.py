# 外部如何访问私有属性？ 通过实例方法调用
class Person(object):
    def __init__(self, name):
        self.__name = name  # 私有属性

    def get_name(self):  # 获取私有属性的方法
        return self.__name
p1 = Person('Bob')  # 实例化
print(p1.get_name())  # 成功获取私有属性name

# 课后作业：请给 Person 类增加一个私有属性 __score，表示分数，再增加一个实例方法 get_grade()，能根据 __score 的值分别
# 返回 A-优秀, B-及格, C-不及格三档。
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score  # 把score属性私有化

    def get_grade(self):  # 获取私有属性的方法
        if self.__score >= 80:
            return "A"
        if self.__score >= 60:
            return "B"
        return "C"

p1 = Person('Bob', 90)  # 实例化类
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print(p1.get_grade())  # 抓取私有属性
print(p2.get_grade())
print(p3.get_grade())

