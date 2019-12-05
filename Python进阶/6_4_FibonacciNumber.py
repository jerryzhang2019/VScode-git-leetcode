# leetcode 509题：求斐波那契数，通常表示为  F(n) 形式的序列，称为斐波纳契数列，使得每个数字是两个前述者的总和，起始0和1。那是，
#  F（0）= 0，F（1）= 1 对于N> 1.F（N）= F（N-1）+ F（N-2） 给定N，计算F(N)。
class Solution():
    def fib(self, N:int) -> int:
        if N <= 1:
            return N
        else:
            return self.fib(N - 1) + self.fib(N - 2)
if __name__ == '__main__': #  添加的main函数
    N = 6
    result = Solution().fib(N) #  把定义的函数实例化
    print(result)
# 斐波那契数列是由 0, 1, 1, 2, 3, 5, 8...构成。请编写一个Fib类，Fib(10)表示数列的前10个元素，print Fib(10)
# 可以打印出数列的前 10 个元素，len(Fib(10))可以正确 返回数列的个数10。
class  Fib(object):
    def __init__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a+b
        self.numbers = L

    def __str__(self):
        return str(self.numbers)
    __repr__ = __str__  # repr面向程序员显示， str面向用户显示

    def __len__(self):
        return len(self.numbers)
f = Fib(10)
print(f)
print(len(f))
# 第一种方法：递归
def FB_tool(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return FB_tool(n-1)+FB_tool(n-2)
def FR(n):
    result_list = []
    for i in range(1, n+1):
        result_list.append(FB_tool(i))
    return result_list
f = FR(10)
print(f)
# 第二种方法:循环
def fl_tool(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a+b
        n -= 1
def FL(n):
    result_list = []
    a, b = 0, 1
    while n > 0:
        result_list.append(b)
        a, b = b, a+b
        n -= 1
    return result_list
f = FL(10)
print(f)
# 第三种迭代解决方案
def fib(self, N:int) -> int:
    if N <= 1:
        return N
    result = [0, 1]
    for i in range(N - 1):
        result.append(sum(result[-2:]))
    return result[-1]
f = fib(1, 11)
print(f)