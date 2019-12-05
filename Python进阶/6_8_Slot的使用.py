#  __slots__的目的是限制当前类所能拥有的属性，如果不需要添加任意动态的属性，使用__slots__也能节省内存。
#  课堂练习
class Student(object):  # 学生类
    __slot__ = ('name', 'name', 'gender', 'score')  # 可以被修改的属性

    def __init__(self, name, gender, score):
        self.name = name
        self.gender = gender
        self.score = score
if __name__ == '__main__':
    s = Student('Bob', 'male', '59')
    s.name = 'Tim'
    s.score = 99
    s.grade = 'A'
    print(s.name, s.score, s.grade)

#  课后练习
#  假设Person类通过__slots__定义了name和gender，请在派生类Student中通过__slots__继续添加score的定义，
#  使Student类可以实现name、gender和score 3个属性。
class Person(object):  # 定义一个人类
    __slots__ = ('name', 'gender')  # 可以被修改的属性

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
class Student(Person):  # 定义一个学生类继承自Person
    __slots__ = ('name', 'gender', 'score')

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)  # super的意思是继承上一个类
        self.name = name
        self.gender = gender
        self.score = score
s = Student('Bob', 'male', '59')   # 实例化
s.name = 'Tim'
s.score = '99'
print(s.score)
print(s.name)
