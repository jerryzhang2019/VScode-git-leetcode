# 题意：给定一个数组nums和一个值val，就地删除该值的所有实例并返回新的长度？
# 不要为另一个数组分配额外的空间，必须通过使用O（1）额外的内存就地修改输入数组来做到这一点。
# 元素的顺序可以更改。超出新长度后剩下的都无所谓。
# 范例1： 给定nums = [3,2,2,3]，val = 3，
# 你的函数应该返回长度= 2，与前两个元素NUMS是2。
# 剩下的长度与返回的长度无关紧要。

class Solution:
    def removeElement(self, nums, val):
        for x in nums[:]:  # [:]表示从集合的头到尾
            if x == val:
                nums.remove(val)
        return len(nums)
if __name__ == '__main__':
    nums = [3, 2, 2, 3, 1]
    result = Solution().removeElement(nums, 3)
    print('The result is:', result)