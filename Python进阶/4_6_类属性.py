# 实例属性每个实例各自拥有，各自独立，而类属性有且只有一份
class Person(object):
    address = 'Earth'  # 类属性是直接绑定在类上

    def __init__(self, name):
        self.name = name
print(Person.address)  # 类属性不需要创建实例， 可以直接访问
p1 = Person('Bob')
p2 = Person('Alice')
print(p1.address)  # 任何实例都可以访问类属性
print(p2.address)  # 任何实例都可以访问类属性
Person.address = 'China'  # 类属性可以被修改
print(p1.address)  # 类的属性已经被修改，由原来的Earth改成了China
# 课后习题
# 任务：请给 Person 类添加一个类属性 count，每创建一个实例，count 属性就加 1，这样就可以统计出一共创建了多少个 Person 的实例。
class Person(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1
p1 = Person('Bob')
print(Person.count)
p2 = Person('Alice')
print(Person.count)
P3 = Person('Tim')
print(Person.count)