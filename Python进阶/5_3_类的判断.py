# 如何判断类的类型？ 使用isinstance()
class Person(object):  # 人类
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
class Student(Person):  # 学生类
    def __init__(self, name, gender, score):
        super(Student,self).__init__(name, gender)  # 继承人类
        self.score = score
class Teacher(Person):  # 老师类
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)  # 继承人类
        self.course = course
p = Person('Tim', 'male')  # 人类的实例化
s = Student('Bob', 'male', '99')  # 学生类的实例化
t = Teacher('Alice', 'female', 'English')  # 老师类的实例化
print(isinstance(p, Person))  # 类的判断
print(isinstance(s, Student))  # 类的判断
print(isinstance(t, Teacher))  # 类的判断
print(isinstance(s, Person))
print(isinstance(s, Teacher))
print(isinstance(t, Student))
print(isinstance(t, object))
print(isinstance(p, object))
print(isinstance(s, object))


