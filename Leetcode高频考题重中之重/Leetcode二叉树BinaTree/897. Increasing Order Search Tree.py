#  Increasing Order Search Tree??
#  给定二叉搜索树，请按顺序重新排列树，以使树中最左边的节点现在成为树的根，每个节点都没有左子节点，只有1个右子节点。
# 注意： 给定树中的节点数将在1到100之间。每个节点将具有一个从0到1000的唯一整数值​​。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def Solution(object):
    def increasingBST(self, root):  # 定义一个解决问题的构造函数
        ans = self.inorder(root)  # 定义一个列表list存储中序遍历得到的值，调用中序遍历函数inorder
        dummy = root = TreeNode(ans[0])  # 定义一个空节点dummy,便于返回整个结果
        for i in range(1, len(ans)):  # 遍历整个ans中的值，重新生成新的只有右节点的树
            root.right = TreeNode(ans[i])  # 赋值，把遍历到的值放在根节点的右孩子上
            root = root.right  # 移动指针：依次移动指针指向右节点
        return dummy

    def inorder(self, root):  # 定义中序遍历，这个是标准的中序遍历方法
        curr, stack = root, []  # 定义当前值为根节点为起始遍历点，定义一个空堆栈stack存储节点
        result = []  # 定义一个数组result存储结果
        while curr or stack:  # 只要当前节点值不为空或者堆栈不为空，则继续循环
            while curr:  # 当前节点值不为空
                stack.append(curr)  # 把遍历到的每一个节点值curr都压进堆栈stack
                curr = curr.left  # 压完栈后，把curr指针指向左孩子，遍历左半边
            # 当所有的节点值都完成了入站后，下一步开始出栈
            curr = stack.pop()  # 把堆栈的值出栈
            result.append(curr.val)  # 把出栈的值一次存储在新的result中
            curr = curr.right  # 当前指针指向右孩子，遍历右半边
        return result

