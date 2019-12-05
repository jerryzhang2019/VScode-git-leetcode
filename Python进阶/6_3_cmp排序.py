# 如何对整型int和字符串str混合排序呢？
import operator
class Student(object):  # 创建学生类
    def __init__(self, name, score):  # 类初始化
        self.name = name  # 对类赋初值
        self.score = score

    def __str__(self):  # __str__()用于显示给用户
        return '(%s:%s)' % (self.name, self.score)
    __repr__ = __str__  # __str__()用于显示给用户 __repr__()用于显示给开发人员

    # def __cmp__(self, s):  # 按照名称比较排序
    #     if self.name < s.name:
    #         return -1
    #     elif self.name > s.name:
    #         return 1
    #     else:
    #         return 0
# 请修改 Student 的 __cmp__ 方法，让它按照分数从高到底排序，分数相同的按名字排序。在python3中没有cmp指令了
    def __it__(self, s):
        if self.score == s.score:
            return operator.gt(self.name, s.name)
        return operator.gt(self.score, s.score)

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 77)]  # 实例化
print(sorted(L))


