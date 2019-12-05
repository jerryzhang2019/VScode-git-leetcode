class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
class Student(Person):
    def __init__(self, name, gender, socre):
        super(Student, self).__init__(name, gender)
        self.score = socre
    def whoAmI(self):
        return 'I am a Student, my name is %' % self.name

print(type(123))
s = Student('Bob', 'Male', '99')
print(type(s))
print(dir(123))  # 打印整数属性
print(dir(s))
print(getattr(s, 'name'))  # 获取指定名字的属性
setattr(s, 'name', 'Adam')  # 设置新的name属性
print(s.name)  # 打印修改后的name属性是'Adam',已经不是原来的Bob
# print(getattr(s, 'age'))  # 获取age属性， 但是属性不存在，会报错
print(getattr(s, 'age', 20))  # 尽管age属性不存在，但是不会报错，返回值会是20

# 如何提供任意额外的关键字参数并绑定到参数？???这个没运行成功
class Person(object):
    def __init__(self, name, gender, **kw):  # **kw的意思是可以传入任意数量的参数
        self.name = name
        self.gender = gender
        for k, v in kw.iteritems():
            setattr(self, k, v)  # setattr的意思是绑定属性
p = Person('Bob', 'Male', age=18, course='Python')
print(p.age)
print(p.course)