from ClassHuman import Human  # 类的调用方法

class Student(Human):  # 定义一个学生Student类，继承Human的属性
    def __init__(self, school, name, age):  # 在构造函数中增加新的变量school，改写子类的构造函数
        self.school = school  # 新的实例变量
        # Human.__init__(self,name, age) # 在子类里面调用父类的构造函数,需要注意的地方是不要忘记添加self,否则会报错
        # 同时上面的方法是不可取的，我们一般不这么使用。但是常用下面的方法

        super(Student, self).__init__(name, age)  # 子类方法调用父类方法，记住关键字super既可以用在构造函数内也可以用在方法内
        
    def do_homework(self):  # 定义一个和父类方法同名的方法,有限调用子类的方法
        super(Student, self).do_homework()  # 使用super关键字调用父类方法
        print('english homework')

student1 = Student('人民路小学','石敢当',18)  # 实例化的时候不需要传入self
student1.do_homework()  # 当子类和父类方法同名，有限显示子类方法

# # print(student1.sum)  # 实例变量
# # print(Student.sum)  # 类变量
# print(student1.name)  # 证明实例变量成功被继承
# print(student1.age)  # 证明实例变量成功被继承

# # student1.get_name()  # 验证方法是否可以被继承