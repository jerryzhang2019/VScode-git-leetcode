import types
def fn_get_grade(self):
    if self.score >= 80:
        return "A"
    if self.socre >= 60:
        return "B"
    return "C"
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
p1 = Person('Bob', 90)
# p1.get_grade = types.MethodType(fn_get_grade, p1, Person)  # 运行失败？？？？/
# print(p1.get_grade())

p2 = Person('Alice', 65)  # 运行失败？？？？
print(p2.get_grade())
