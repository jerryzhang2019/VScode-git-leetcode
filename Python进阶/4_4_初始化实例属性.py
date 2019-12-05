# 任务：请定义Person类的__init__方法，除了接受 name、gender 和 birth 外，还可接受任意关键字参数，
# 并把他们都作为属性赋值给实例。
class Person(object):
    def __init__(self, name, gender, birth,**kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        for k, v in kw.iteritems():  # 运行不成功？？？？？
            setattr(self, k, v)
xiaoming = Person('Xiao Ming', 'Male', '1990-01-01', job = 'Student')
print(xiaoming.name)
print(xiaoming.job)
