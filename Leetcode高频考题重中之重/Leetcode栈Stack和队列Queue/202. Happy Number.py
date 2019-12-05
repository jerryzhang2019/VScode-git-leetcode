# 题意：编写算法以确定数字是否为“ happy”。
# 一个快乐的数字是由以下过程定义的数字：以任何正整数开头，用该数字的平方和代替该数字，然后重复该过程，
# 直到该数字等于1（它将停留在该位置），否则将循环在不包含1的循环中无休止地循环。以1结尾的那些数字是快乐数字。
# 例： 输入： 19
#  输出： true
#  说明：
#  1 2 + 9 2 = 82
# 8 2 + 2 2 = 68
# 6 2 + 8 2 = 100
# 1 2 + 0 2 + 0 2 = 1
class Solution:
    def isHappy(self, n):
        cycle = set()  # 定义一个空的集合
        while n != 1 and n not in cycle:
            cycle.add(n)
            n = sum(pow(int(i), 2) for i in str(n))  # pow意思是:pow() 方法返回 xy（x的y次方） 的值。
        return n == 1  # 最终输出为1
if __name__ == '__main__':
    n = 19
    result = Solution().isHappy(n)
    print(result)  # 输出结果为True

