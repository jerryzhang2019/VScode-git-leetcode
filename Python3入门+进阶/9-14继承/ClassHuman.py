class Human():  # 定义一个人父类
    sum = 0  # 定义一个变量sum并赋初值为0
    def __init__(self, name, age):  # 定义一个构造函数
        self.name = name  # 实例变量
        self.age = age  # 实例变量

    def get_name(self):  # 定义一个方法获取学生名字
        print(self.name)