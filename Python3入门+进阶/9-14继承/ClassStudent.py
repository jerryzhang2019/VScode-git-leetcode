from ClassHuman import Human  # 类的调用方法

class Student(Human):  # 定义一个学生Student类，继承Human的属性

    pass
    def do_homework(self):
        print('english homework')
student1 = Student('石敢当',18)
print(student1.sum)
print(Student.sum)
print(student1.name)
print(student1.age)
