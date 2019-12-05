# 合并两个排序链表？并将其作为新列表返回。应该通过将前两个列表的节点拼接在一起来创建新列表
# 例：
# 输入： 1-> 2-> 4，1-> 3-> 4
#  输出： 1-> 1-> 2-> 3-> 4-> 4
class ListNode:
    def __init__(self, x):  # x 是什么意思？？？如何给X赋值？？？/
        self.val = x
        self.next = None

    def mergeTwoLists(self, l1, l2):
        dummy = curr = ListNode(0)  # dummy的意思是虚拟变量，作用是有利于最后打印总的链表

        while l1 and l2:  # 当两个链表都不为空的时候，执行下一步
            if l1.val < l2.val:
                curr.next = l1  # 赋值步：l1中的值存储到curr中
                l1 = l1.next  # l1的指针指向下一位
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next  # 更新curr的指针，一个循环结束后，把当前指针curr指向下一步

        curr.next = l1 or l2  # 当l1里的值都小于l2时，循环结束后，l2依然存在，需要把剩余的l2都插入到curr链表中（赋值）
        return dummy.next  # 返回合并后的链表

if __name__ == '__main__':
    l1 = [1, 2, 4]
    l2 = [3, 5, 7]
    result = ListNode().mergeTwoLists(l1, l2)
    print('The result is:', result)