# 单值二叉树？？？二进制树univalued如果树中的每个节点具有相同的值， 返回true 当且仅当给定的树univalued。
# Example 1:
# Input: [1,1,1,1,1,null,1]
# Output: true
# Example 2:
# Input: [2,2,2,5,2]
# Output: false
class Solution:
    def isUnivalTree(self, root):
        def rec(root, val):  # 定义一个构造函数rec遍历整个二叉树

            if not root:  # 特列：如果根节点不存在，为空，则属于单一值
                return True

            if root.val == val:  # 如果根节点值和给定值相等，遍历整个树都相等，可以判断为单一值的树
                return rec(root.left, val) and rec(root.right, val)  # 递归整个左子树和右子树
            else:
                return False

        return rec(root, root.val)  # 实例化：调用rec函数判断root值是否是和root.val值一直相等