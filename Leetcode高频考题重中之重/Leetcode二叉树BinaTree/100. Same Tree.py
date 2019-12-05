# 给定两个二进制树，编写一个函数来检查它们是否相同?
# 如果两个二叉树在结构上相同并且节点具有相同的值，则认为它们是相同的。
# Example 1:
# Input:     1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
# Output: true
# Example 2:
# Input:     1         1
#           /           \
#          2             2
#         [1,2],     [1,null,2]
# Output: false
# Example 3:
# Input:     1         1
#           / \       / \
#          2   1     1   2
#         [1,2,1],   [1,1,2]
# Output: false
class Solution:
    def isSomeTree(self, p, q):
        if p is None and q is None:  # 当p树和q树都为空时，则两个树相等
            return True  # 两个树相等
        if p is not None and q is not None:  # 如果树p和q数都不为空，则判断节点值是否相等
            return p.val == q.val and self.isSomeTree(p.left, q.left) and self.isSomeTree(p.right, q.right)
# 数p和数q的节点值相等，同时p树的左子孩子和q树的左子孩子相等,同时p树的右孩子和q树的右孩子相等，采用递归的方法
        return False  # 返回 False????为什么？？？？