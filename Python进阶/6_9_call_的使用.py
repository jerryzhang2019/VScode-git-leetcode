#  课堂例子
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __call__(self, friend):  # 一个类实例变成可调用函数的例子
        print('My name is%...'% self.name)
        print('My friend is%'%friend)
if __name__ == '__main__':
    p = Person('Bob', 'male')
    print('Tim')  # 可调用的函数
#  课后习题：对斐波那契额数的优化
class Fib(object):
    def __call__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        return L
if __name__ == '__main__':
    f = Fib()
    print(f(10))  # 打印斐波那契数列的前十项

# 如何只返回斐波那契额数的某个特定的值？
class Solution:
    def fib(self, N:int) ->int:
        if N <= 1:
            return N
        else:
            return self.fib(N -1) + self.fib(N - 2)
if __name__ == '__main__':
    f = Solution().fib(10)
    print(f)
