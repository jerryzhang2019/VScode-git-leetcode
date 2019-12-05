# 类属性和实例属性重名时，实例属性优先级更高，他将屏蔽掉对类属性的访问
class Person(object):
    address = 'Earth'  # 定义类属性

    def __init__(self, name):
        self.name = name
p1 = Person('Bob')
p2 = Person('Alice')
print('Person.address = ' + Person.address)

p1.address = 'China'  # 把实例p1的属性修改为China
print('p1.address = ' + p1.address)
print('Person.address = ' + Person.address)  # 类属性并没有根本改变
print('p2.address = ' + p2.address)  # 实例2的类属性还是没改变

del p1.address  # 删除实例p1的类属性
print(p1.address)  # 证明了在实例上修改类属性，它实际上并没有修改类属性，而是给实例绑定了一个实例属性

# 课后练习：如果把类属性设计为私有，通过在属性名字前面加两个下划线__(),这样实例变量就在外部无法修改了
class Person(object):
    __count = 0  # 把类的属性设置为私有

    def __init__(self, name):
        self.name = name
        Person.__count += 1
        print(Person.__count)
p1 = Person('Bob')
p2 = Person('Alice')
try:
    print(Person.__count)
except:
    print('AttributeError')


