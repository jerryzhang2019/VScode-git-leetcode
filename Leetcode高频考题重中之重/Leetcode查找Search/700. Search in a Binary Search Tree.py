# 给定二叉搜索树（BST）的根节点和一个值。您需要在BST中找到该节点的值等于给定值的节点。返回以该节点为根的子树。
# 如果该节点不存在，则应返回NULL。
# 例如， 给定树：
#         4
#        / \
#       2   7
#      / \
#     1   3
# 搜索的值：2
# 您应该返回以下子树：
#       2
#      / \
#     1   3
# 在上面的示例中，如果我们要搜索值5，由于没有带值的节点5，我们应该返回NULL。
# 请注意，空树由表示NULL，因此您会看到预期的输出（序列化的树格式）为  []，而不是null。
# BST右一个重要的性质，根节点的左孩子都小于根节点的值，根记得点的右孩子都大于根节点的值
class Solution:
    def searchBST(self, root, val):
        if root is None:  # 如果根节点为空，则返回空树
            return None

        elif root.val == val:  # 如果根节点值和给定值相等，则返回根节点
            return root

        elif val < root.val:  # 如果给定值val小于根节点值，则向左子树搜索（二分搜索树的性质）
            return self.searchBST(root.left, val)  # 递归搜索左子树
        else:  # 否则的情况就是给定值val的值大于根节点的值，则向右子树搜索（二分搜索树性质）
            return self.searchBST(root.right, val)  # 递归搜索右子树

