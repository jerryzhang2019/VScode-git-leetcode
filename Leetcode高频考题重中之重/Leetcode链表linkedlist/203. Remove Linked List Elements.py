# 删除链接列表元素？从值val的整数链接列表中删除所有元素。
# 例：
# 输入：  1-> 2-> 6-> 3-> 4-> 5-> 6，val = 6
#  输出： 1-> 2-> 3-> 4-> 5
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(float('-inf'))  # 定义一个虚拟变量

        dummy.next = head  # 虚拟变量dummy.next指向head头节点
        previous = dummy  # 定义previous变量指向dummy
        current = dummy.next  # 定义current变量指向dummy.next

        while current:  # 只要current存在就可以执行while循环
            if current.val == val:  # 如果当前值和给定值相等
                previous.next = current.next  # 赋值回指，把current.next指针指向current前面一个节点previous
            else:  # 如果当前值和给定值不相等
                previous = current  # previous往后挪一步，指向current
            current = current.next  # 同时current往后挪一步，指向current.next
        return dummy.next
if __name__ == '__main__':
    head = [1, 2, 6, 3, 4, 5, 6]
    val = 6
    result = Solution().removeElements(head, val)
    print(result)
