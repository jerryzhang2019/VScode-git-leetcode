# 从排序数组中删除重复项：给定一个已经排序的数组，就地删除重复项，以使每个元素只出现一次并返回新的长度，不为另一个数组分配
# 额外的空间，必须通过使用O（1）额外的内存就地修改输入数组来做到这一点。
class Solution:
    def removeDuplicates(self, nums):  # 定义一个方法
        curr_idx = 0  # 定义一个变量索引，初始值为0

        while curr_idx < len(nums) - 1:  # 定义while循环的长度，索引值从0开始，所有总长度为n-1
            if nums[curr_idx] == nums[curr_idx + 1]:  # 判断索引当前值和下一个值是否相等，如果相等则删除
                del nums[curr_idx]  # 执行删除操作
                curr_idx -= 1  # 删除后索引值逐次减一 ？？？？这里不是很理解
            curr_idx += 1  # 开始下一个循环之前把索引值+1,然后开始下一循环
        return len(nums)  # 循环结束后返回剩余数组的长度

if __name__ == '__main__':
    # Test case1
    nums = [1, 1, 2]
    result = Solution().removeDuplicates(nums)
    print('Test case result is: ', result)
    print('after delete the nums is:', nums)
    # Test case2
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result = Solution().removeDuplicates(nums)
    print('Test case result is: ', result)
    print('after delete the nums is:', nums)
