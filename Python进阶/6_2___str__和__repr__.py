# 任务:
# 请给Student类定义__str__和__repr__方法，使得能打印出<Student: name, gender, score>
# 考察知识点： __str__()用于显示给用户 __repr__()用于显示给开发人员
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def __str__(self):  # str()用于显示给用户
        return '(Student: %s,%s, %d)'%(self.name, self.gender, self.score)
    __repr__ = __str__
s = Student('Bob', 'Male', 88)
print(s)