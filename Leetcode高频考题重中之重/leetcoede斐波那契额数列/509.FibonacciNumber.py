'''
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is
# the sum of the two preceding ones, starting from 0 and 1. That is, F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1. Given N, calculate F(N)。
'''
# 问题1： 打印斐波那契的指定的莫一个数
class Solution:
    def fib(self, N:int) -> int:
        if N <= 1:
            return N
        else:
            return self.fib(N - 1) + self.fib(N - 2)
if __name__ == '__main__':
    N = 5
    result = Solution().fib(N)  # 只打印某一个数
    print(result)

# 问题2：打印斐波那契数的前N个数？比如打印前10个数等等

class Fib(object):
    def __init__(self, num):
        a, b, L = 0, 1, []
        for i in range(num):
            L.append(a)
            a, b = b, a + b
        self.numbers = L

    def __str__(self):
        return str(self.numbers)

    __repr__ = __str__

result = Fib(10)
print(result)

