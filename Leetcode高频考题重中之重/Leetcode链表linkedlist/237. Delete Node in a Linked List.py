# 删除链表中节点编写一个函数以删除单链接列表中的节点（尾部除外），仅授予对该节点的访问权限。
# 给定的链表-head = [4,5,1,9]，如下所示：
# 范例1：输入： head = [4,5,1,9]，node = 5  输出： [4,1,9] 说明：第二个节点的值为5，链表应该变为4-> 1-> 9调用函数后。
# 范例2：输入： head = [4,5,1,9]，node = 1 输出： [4,5,9] 说明：第三个节点的值为1，链接列表应变为  4-> 5-> 9调用函数后。
# 注意：1.链表将至少包含两个元素。2.所有节点的值都是唯一的。3.给定的节点将不是尾部，并且将始终是链表的有效节点。
# 4.不要从函数中返回任何东西。
# class Solution:
#     def deleteNode(self, node):
#         node.val = node.next.val  # 意思是直接赋值替换，把节点后面的值直接覆盖掉当前节点的值
#         node.next = node.next.next  # 当前节点的下一个的指针指向下下一个节点，跳过node.next节点，指向下一个节点
# 我使用作为元素给出的ListNode创建一个列表来验证两者之间的区别：
class My_List(object):
    def __init__(self, x):
        self.first_node = x
        self.last_node = x

    def add(self, x):
        self.last_node.next = x
        self.last_node = self.last_node.next

    def print(self):
        temp = self.first_node
        index = 0
        while temp is not None:
            print('%s-%s' % (index, temp.val))
            temp = temp.next

class ListNode:  # 定义节点类
    def __init__(self, x):
        self.val = x
        self.next = None

my_list = My_List(ListNode('start'))  # 实例化
dd = {}  # use this dict to keep reference to each element
for i in range(5):
    dd[i] = ListNode('item-%s' % i)
    my_list.add(dd[i])
print('The old linked list is:')
my_list.print()  # 打印链表

# 测试案例#1:删除节点3
node = dd[3]  # suppose I want to delete this node
node = node.next  # this is the first thought I took
print('The new linked list is below:')
my_list.print()

# 测试案例# 2：删除节点3
node = dd[3]
node.val = node.next.val  # 意思是直接赋值替换，把节点后面的值直接覆盖掉当前节点的值
node.next = node.next.next  # 当前节点的下一个的指针指向下下一个节点，跳过node.next节点，指向下一个节点
print('The new linked list is below:')
my_list.print()