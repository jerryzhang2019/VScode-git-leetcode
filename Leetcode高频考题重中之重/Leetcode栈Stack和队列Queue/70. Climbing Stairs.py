# 堆栈stack的问题：爬楼梯--您正在爬楼梯。它需要n步才能到达顶部。每次您可以爬1或2步。您可以通过几种不同的方式登顶？
# 如何联想到使用斐波那契数列？？？
class Solution:
    def climbStairs(self, n):  # 楼梯数是n
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current  # 结果符合斐波那契数列规律???为什么能够想到？？？
        return current

if __name__ == '__main__':
    n = 5
    result = Solution().climbStairs(n)
    print('The result is:', result)