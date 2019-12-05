# 求二叉树的节点的表兄弟？？？？
# 在二叉树中，根节点位于depth 0，每个深度k节点的子节点位于depth k+1。如果二叉树的两个节点具有相同的深度，但是具有不同的
# 父级，则它们是表亲。我们给出了root具有唯一值的二叉树的，以及树 中两个不同节点的值x 和y。
# 返回  true 当且仅当对应值的节点x和y是堂兄弟。
# Example 1:
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# Example 2:
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
class Solution(object):
    def isCousins(self, root, x, y):
        self.ans = []  # 定义一个临时变量数组存储深度遍历中的节点值

        def DFS(node, x, k, parent):  # 定义深度优先遍历函数
            if node.val == x:  # 如果节点值和给定值x相等
                self.ans.append(k)  #
                self.ans.append(parent.val)  # 紧随存储父亲节点值
            else:
                if node.left:  # 如果左孩子存在
                    DFS(node.left, x, k+1, node)  # 递归左孩子节点
                if node.right:  # 如果右孩子存在
                    DFS(node.right, x, k+1, node)  # 递归右孩子节点

            DFS(root, x, 0, root)
            DFS(root, y, 0, root)

            return self.ans[0] == self.ans[2] and self.ans[1] != self.ans[3]





