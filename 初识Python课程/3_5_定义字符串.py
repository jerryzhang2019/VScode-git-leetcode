# 字符串表示方法？字符串可以用''或者""括起来表示。
# 1.如果字符串本身包含'怎么办？比如我们要表示字符串 I'm OK ，这时，可以用" "括起来表示：
# 2.如果字符串包含"，我们就可以用' '括起来表示：
# 3.如果字符串既包含'又包含"怎么办？，就需要对字符串的某些特殊字符进行“转义”，Python字符串用\进行转义。
# 一个\表示这是一个普通字符，不代表字符串的起始，注意：转义字符 \ 不计入字符串的内容中。
# 常用的转义字符还有：\n 表示换行，\t 表示一个制表符，\\ 表示 \ 字符本身
# 任务：请将下面两行内容用Python的字符串表示并打印出来：
# Python was started in 1989 by "Guido". Python is free and easy to learn.
s = 'Python was started in 1989 by \" Guido\".\n Python is free and easy to learn'
print(s)
