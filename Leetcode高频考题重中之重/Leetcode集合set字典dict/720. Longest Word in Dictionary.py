# 720:字典中最长的单词??
# 给定words代表英语词典的字符串列表，找到其中最长的单词words，一次可以由中的其他单词构成一个字符words。
# 如果有多个可能的答案，请以最小的词典顺序返回最长的单词。
# 如果没有答案，则返回空字符串。
# 范例1：输入： 单词= [“ w”，“ wo”，“ wor”，“ worl”，“世界”]
# 输出： “世界”
#  说明：
# 单词“世界”可以一次由“ w”，“ wo”，“ wor”和“ worl”建立一个字符。
# 范例2：输入： 单词= [“ a”，“香蕉”，“ app”，“ appl”，“ ap”，“ apply”，“ apple”]
# 输出： “ apple”
#  说明：
# “ apply”和“ apple”都可以从词典中的其他单词构建。但是，“苹果”在字典上比“应用”小。