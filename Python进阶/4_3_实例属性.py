# 任务：请创建包含两个 Person 类的实例的 list，并给两个实例的 name 赋值，然后按照 name 进行排序。
class Person(object):
    pass
p1 = Person()
p1.name = 'Bart'
p2 = Person()
p2.name = 'Adam'
p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1, lambda p1, p2: cmp(p1.name, p2.name))  # 运行不成功，由于cmp命令不存在了？？？？？

print(L2[0].name)
print(L2[1].name)
print(L2[2].nmae)