# 有效的括号判断？？
# 由于只包含字符的字符串'('，')'，'{'，'}'，'['和']'，确定输入字符串是有效的。
# 输入字符串在以下情况下有效：
# 开括号必须用相同类型的括号封闭。
# 开括号必须以正确的顺序关闭。
# 请注意，空字符串也被视为有效。
# 范例1：
# 输入： “（）”
#  输出： true
class Solution:
    def isValid(self, s):
        stack = []  # 定义一个堆栈存储括号
        match = {'(':')','[':']','{':'}'}  # 定义一个字典其中包含所有的括号

        for char in s: # 开启循环查找
            if char in match:  # 判断输入的符号在字典match中
                stack.append(match[char])  # 把循环到的符号依次压栈
            else:
                if len(stack) == 0 or stack.pop() != char:  # 错误条件有两种：1-堆栈长度为零，2.出栈的符号和char中的符号不匹配
                    return False  # 返回错误意思是符号不匹配
        return len(stack) == 0  # 排除一种错误情况是stack堆栈中已经空了，但是还有剩余符号在char中，则返回错误
