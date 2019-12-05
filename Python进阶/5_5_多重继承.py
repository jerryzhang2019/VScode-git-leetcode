# 多重继承的意思是从多个父类继承，不只限于一个父类
# 通过多重继承 定义会打篮球的学生，会踢足球的老师
class Person(object):  # 人类
    pass
class Student(Person):  # 学生类
    pass
class Teacher(Person):  # 教师类
    pass
class SkillMixin(object):  # 技能
    pass
class BasketballMixin(SkillMixin):  # 篮球技能继承自技能类
    def skill(self):
        return 'basketball'
class FootballMixin(SkillMixin):  # 足球技能继承自技能类
    def skill(self):
        return 'football'
class BStudent(Student, BasketballMixin):  # 这个类同时继承了学生类和篮球技能类
    pass
class FTeacher(Teacher, FootballMixin):  # 这个类同时继承了教师类和足球技能类
    pass
s = BStudent()
print(s.skill())
t = FTeacher()
print(t.skill())