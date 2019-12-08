#  课堂练习
class Person(object):  # 人类
    def __init__(self, name, gender):  # 构造函数
        self.name = name
        self.gender = gender
class Student(Person):  # 学生类是继承了父类Person的属性，这样是内部继承，如何从外部继承呢？
    def __init__(self, name, gender, score):  # 构造函数
        super(Student, self).__init__(name, gender)
        self.score = score
class Teacher(Person): # 老师类
    def __init__(self, name, gender, course): # 构造函数
        super(Teacher, self).__init__(name, gender)
        self.course = course

t = Teacher('Alice', 'Female', 'English')  # 对老师类实例化
s = Student('jerry', 'male', '99')  # 学生类
print(t.name)
print(t.course)
print(s.name)
print(s.gender)
print(s.score)