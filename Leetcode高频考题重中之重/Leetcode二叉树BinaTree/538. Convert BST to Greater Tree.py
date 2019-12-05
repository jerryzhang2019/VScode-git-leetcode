# 将BST转换为更大的树？给定二叉搜索树（BST），将其转换为更大的树，以便将原始BST的每个关键字更改为原始关键字，
# 再加上大于BST中原始关键字的所有关键字的总和。总体思路是进行逆序遍历，并在创建新树时添加总和。
# Example:
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root):
        def generate_greater_tree(node):
            if not node:  # 如果节点为空，则返回空
                return None
            right = generate_greater_tree(node.right)  # 递归遍历整个树的右节点

            self.sum += node.val  # 求节点的和
            new_node = TreeNode(self.sum)  # 新的根节点值

            new_node.right = right  # 新的节点右孩子仍然使用原来的值
            new_node.left = generate_greater_tree(node.left)  # 使用递归产生新的树的左子树的值

            return new_node  # 返回新的根节点
        self.sum = 0  # 定义初始值为0
        return generate_greater_tree(root)  # 返回新树的根节点





