# 判断但链表是不是回文？给定一个单链表，确定它是否是回文。
# 范例1： 输入： 1-> 2  输出： false
# 范例2：输入： 1-> 2-> 2-> 1  输出： true
# 跟进：您能在O（n）时间和O（1）空间中做到吗？
class Solution:
    def isPalindrome(self, head):
        if head is None:  # 首先判断链表是否为空，如果为空则是回文链表
            return True
        fast = slow = head  # 定义一个快慢指针，并且同时都指向头节点
        stack = []  # 定义一个空堆栈存储链表的前半部分

        while fast and fast.next:  # 判断fast和fast都存在时
            stack.append(slow.val)  # slow表示链表的前半部分，fast表示链表的后半部分，把slow前半部分压入栈
            slow = slow.next  # 慢指针一次移动一个位置
            fast = fast.next.next  # 快指针一次移动两个位置

        while fast:  # 判断当只有fast没有fast,next的时候，表示fast已经移到了尾部
            slow = slow.next  # 慢指针移动最后一个位置，完成堆栈的工作，成功把连报表分为二

        while slow:  # 这个时候慢指针移动到链表的后半部分的第一个位置，准备和对阵的第一个值进行比较
            top = stack.pop()  # 出栈，链表前半部分压入堆栈的值出栈，栈顶值是最后压进去的值
            if top != slow.val:  # 如果栈顶值和后半部分第一个值不相等，则返回假，如果相等则继续比较，直到全部比完
                return False
            slow = slow.next  # 如果两个值相等，则指针后移，继续完成后面所有的比较
        return True

