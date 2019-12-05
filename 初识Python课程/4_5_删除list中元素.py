# 任务：注意右边编辑器代码中 list 如下：L = ['Adam', 'Lisa', 'Paul', 'Bart']Paul的索引是2，Bart的索引是3，如果我们要把
# Paul和Bart都删掉，请解释下面的代码为什么不能正确运行：L.pop(2) L.pop(3) 怎样调整代码可以把Paul和Bart都正确删除掉？
L = ['Adam', 'Lisa', 'Paul', 'Bart']
L.pop(2)
print(L)
L.pop(2)
print(L)