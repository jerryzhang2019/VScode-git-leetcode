# 二分查找？？折半查找
# 给定一个排序（以升序）整数数组nums的n元素和一个target值，写一个函数来搜索target在nums。
# 如果target存在，则返回其索引，否则返回-1。
# 范例1：
# 输入： nums = [-1,0,3,5,9,12]，target= 9
#  输出： 4
#  说明：存在9 nums且其索引为4
class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1  # 定义搜索数组的起始地址left和结束地址right

        while left <= right:  # 当起始地址left小于等于right的时候，持续循环，知道两个值相等则结束
            mid = (left + right) // 2  # 计算中间位置的值

            if nums[mid] < target:  # 如果计算的中间值小于目标值，则左边起始搜索值从中间值加一开始继续搜索
                left = mid + 1
            elif nums[mid] > target:  # 如果中间值大于目标值，则右边起始搜索值从中间值减一开始搜索，逼近目标值
                right = mid -1
            else:
                return mid  # 如果中间值和目标值相等，则直接返回中间值的索引
        return -1  # 如果没有找到，则返回-1
