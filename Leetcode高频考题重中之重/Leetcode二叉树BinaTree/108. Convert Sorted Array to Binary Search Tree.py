# 给定一个数组，其中元素按升序排序，请将其转换为高度平衡的BST。
# 对于此问题，将高度平衡的二叉树定义为一个二叉树，其中每个节点的两个子树的深度相差不超过1。
# 例：
# 给定排序数组：[-10，-3,0,5,9]，
# 一个可能的答案是：[0，-3,9，-10，null，5]，它表示以下高度平衡的BST：
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:  # 边界情况判断
            return None

        mid = len(nums)//2  # 取出中间位置
        root = TreeNode(nums[mid])  # 确定根节点，数组中间位置的值即为根节点

        root.left = self.sortedArrayToBST(nums[:mid])  # 采用递归的方法确定左孩子
        root.right = self.sortedArrayToBST(nums[mid+1:])  # 递归确定右孩子

        return root  # 循环结束后返回节点，即为整个树，因为每个循环都会以root.left为根节点为root.



