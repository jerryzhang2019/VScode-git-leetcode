# 两个数组的交集：注意： 结果中的每个元素都必须是唯一的。结果可以是任何顺序。
# 方法1：蛮力搜索
class Solution:
    def intersection(self, nums1, nums2):
        res = []  # 定义一个存储结果的变量
        for i in nums1:
            if i in nums2 and i not in res:
                res.append(i)
        return res
if __name__ == '__main__':
    # Test case1
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    result = Solution().intersection(nums1, nums2)
    print('The test resutl is:', result)
    # Test case2
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    result = Solution().intersection(nums1, nums2)
    print('The test resutl is:', result)
