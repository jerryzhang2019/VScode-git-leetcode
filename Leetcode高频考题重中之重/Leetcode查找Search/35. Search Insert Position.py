# 给定排序数组和目标值，如果找到目标，则返回索引。如果不是，则返回按顺序插入索引的位置的索引。
# 您可以假设阵列中没有重复项。
# 范例1：
# 输入： [1,3,5,6]，5
#  输出： 2
# 范例2：
# 输入： [1、3、5、6]，2
#  输出： 1
class Solution:
    # def searchInsert(self, nums, target):  # 方案一：暴力搜索 时间复杂度O(n)
    #     for i in range(len(nums)):
    #         if nums[i] >= target:
    #             return i
    #     return len(nums)

    def searchInsert(self, nums, target):  # 方案二：二分搜索 时间复杂度O(logn)
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

if __name__ == '__main__':
    # Test case#1
    nums = [1, 3, 5, 6]
    target = 5
    result = Solution().searchInsert(nums, target)
    print('The new nums is:', nums)
    print('The result is:', result)
    # Test case#2
    nums = [1, 3, 5, 6]
    target = 2
    result = Solution().searchInsert(nums, target)
    print('The new nums is:', nums)
    print('The result is:', result)



