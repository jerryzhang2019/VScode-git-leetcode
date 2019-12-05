# 另一棵树的子树？？
# 给定两个非空二叉树t和s，检查树是否s具有完全相同的结构和节点值用的子树t。子树小号是一个树由一个节点的t
# 和所有这个节点的后代的。树t也可以被认为是其自身的子树。
# Example 1:
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
# Example 2:
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.
class Solution:
    def isSameTree(self, p, q):  # 构造函数的功能时判断两个二叉树是相同的
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # 相同的条件：节点值相等，左孩子节点相同， 右孩子节点相同
        return p is q  # 结论二叉树p和二叉树q相同

    def isSubtree(self, s, t):
        if not s:  # 如果二叉树s不为空
            return False
        if self.isSameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


