# 求链表的中点：定一个带有头节点的非空单链表head，返回链表的中间节点。
# 如果有两个中间节点，则返回第二个中间节点。
#  范例1：输入：[1,2,3,4,5]  输出：此列表中的节点3（序列化：[3,4,5]）
# 返回的节点的值为3。（此节点的法官序列化为[3,4,5]）。
# 请注意，我们返回了ListNode对象ans，例如：
# ans.val = 3，ans.next.val = 4，ans.next.next.val = 5，ans.next.next.next = NULL。

# 范例2：输入：[1,2,3,4,5,6] 输出：此列表中的节点4（序列化：[4,5,6]）
# 由于列表具有两个中间节点，其值分别为3和4，因此我们返回第二个。
# 注意：给定列表中的节点数将在1 和之间100。

class Solution:
    def midNode(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow