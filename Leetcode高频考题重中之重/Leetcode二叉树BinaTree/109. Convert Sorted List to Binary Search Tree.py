# 给定一个单链列表，其中元素按升序排序，请将其转换为高度平衡的BST。
# 对于此问题，将高度平衡的二叉树定义为一个二叉树，其中每个节点的两个子树的深度相差不超过1。
# 例：
# 给定排序的链表：[-10，-3,0,5,9]，
# 一个可能的答案是：[0，-3,9，-10，null，5]，它表示以下高度平衡的BST：
#       0
#      / \
#    -3   9
#    /  /
#  -10  5
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:  # 套用
    def sortedListToBST(self, head:ListNode) -> TreeNode:
        if not head:  # 边界案例
            return None
        if not head.next:  # 边界案例
            return TreeNode(head.val)

        def findMid(self, head):  # 子函数-特定的功能函数
            prev = None  # 提前定义3个指针变量，prev是一个虚节点
            slow = fast = head  # 快慢指针都从头节点开始移动

            while fast and fast.next: # 当这两个节点都存在时继续循环，否则跳出循环
                prev = slow  # prev一次循环跳一格
                slow = slow.next  # 慢指针slow一次跳一格
                fast = fast.next.next  # 快指针fast一次跳2格
            prev.next = None  # while循环结束的条件必然时prev的下一个节点为空，prev指针移动到中间位置
            return slow  # 循环全部结束后，指针slow遍历了半个链表，停止在中间位置mid

        mid = findMid(head)  # 找到链表的中间位置索引,调用函数

        root = self.TreeNode(mid.val)  # 找到根节点
        # 为什么适用切片法？是因为链表的是按照升序排列的，同时BST的性质又是左孩子都小于根节点，右孩子都大于根节点（性质）
        root.left = self.sortedListToBST(head)  # 左孩子，head是第一个左孩子，切片法，从head到mid-1都是左孩子
        root.right = self.sortedListToBST(mid.next)  # 右孩子，从mid.next到结尾都是右孩子
        return root  # 每个循环返回一个根节点，所有循环运行完，可以返回整个二叉树的所有节点，既是一个完整的二叉树




# class Solution:  # 方案2
#     def sortedListToBST(self, head: ListNode) -> TreeNode:
        # if head is None:  # 边界条件链表的头节点为空，是一个空的二叉树
        #     return None
        # if head.next is None:  # 边界条件
        #     return TreeNode(head.val)  # 返回链表的头节点即是二叉树的根节点
        #
        # prev = None  # 定义一个虚拟节点
        # slow = head  # 定义一个慢指针指向头节点
        # fast = head.next  # 定义一个快指针指向下一个节点
        #
        # while fast and fast.next:  # 当头节点后的两个节点都有值时，一直执行循环
        #     prev = slow  # 三个指针一次向后移动一位
        #     slow = slow.next
        #     fast = fast.next.next
        #
        # if prev:  # 如果prev虚节点一直存在,则循环直到终点prev.next是空
        #     prev.next = None
        # else:
        #     head = None
        #
        # node = TreeNode(slow.val)  # 根节点
        # node.left = self.sortedListToBST(head)  # 递归place左子树
        # node.right = self.sortedListToBST(slow.next)  # 递归place右子树
        #
        # return node  # 循环结束返回根节点
