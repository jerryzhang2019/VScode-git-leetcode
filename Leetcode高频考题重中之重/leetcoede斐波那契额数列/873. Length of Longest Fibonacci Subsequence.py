#  Length of Longest Fibonacci Subsequence 求最长斐波那契子序列的长度？
class Solution:
    def lenLongestFibSubseq(self, A):
        s = set(A)  # 定义一个集合
        n = len(A)  # 确定循环的长度
        result = 0  # 定义一个存储结果的变量
        for i in range(n-1):  # 由于初始位是从0开始，所以总共循环次数是n-1次
            for j in range(i + 1, n):
                a, b = A[i], A[j]
                count = 2
                while a + b in s:
                    a, b = b, a + b
                    count += 1
                    result = max(result, count)
        return result if result > 2 else 0
if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7, 8]  # 测试案例
    s = Solution().lenLongestFibSubseq(A)  # 类的实例化
    print(s)  # 测试结果应该为5,5为斐波那契数列的长度
