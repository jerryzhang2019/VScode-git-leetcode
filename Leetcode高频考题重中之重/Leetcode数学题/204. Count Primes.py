# 统计素数的个数？？
# 计算小于非负数n的质数数。
# 例：
# 输入： 10
#  输出： 4
#  说明：有4个质数小于10，它们是2、3、5、7。
class Solution:
    def countPrimes(self, n):
        if n <= 1:
            return 0
        nums = [None] * n
        nums[0] = False
        nums[1] = False

        for i in range(n):
            if nums[i] == None:
                nums[i] = True

                for j in range(i + i, n, i):
                    nums[j] = False
        return sum(nums)