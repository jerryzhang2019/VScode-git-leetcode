# 课堂练习题 使用whoAmI方法查找类的多态
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def whoAmI(self):
        return 'I am a Person, my name is %s' % self.name
class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name
class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

    def whoAmI(self):
        return 'I am a Teacher, my name is %s' % self.name

def whoAmI(x):
    print(x.whoAmI())
p = Person('Tim', 'male')
s = Student('Bob', 'male', '99')
t = Teacher('Alice', 'female', 'English')

whoAmI(p)
whoAmI(s)
whoAmI(t)

# 例子
class Book(object):
    def whoAmI(self):
        return 'I am a book'
# 课后习题 ???????????
import json
f = open('/path/to/file.json', 'r')
print(json.load(f))

import json
class Student(object):
    def read(self):
        return r'["Tim", "Bob", "Alice"]'
s = Student()  # 实例化学生类
print(json.loads(s))

