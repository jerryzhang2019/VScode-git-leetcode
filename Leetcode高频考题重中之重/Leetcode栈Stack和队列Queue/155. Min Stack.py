# 求最小堆栈stack?
class MinStack:
    def __init__(self):
        self.s = []  # 定义一个存储输入的原堆栈
        self.minS = []  # 定义一个存储最小值的新堆栈

    def push(self, x):
        n = len(self.s)
        if n == 0:
            self.minS.append(x)
        else:
            lastmin = self.minS[-1]
            if x < lastmin:
                self.minS.append(x)
        self.s.append(x)

    def pop(self):
        if self.s[-1] == self.minS[-1]:
            self.minS.pop()
        self.s.pop()

    def top(self):
        if self.s:
            return self.s[-1]
        else:
            return None

    def getMin(self):
        if self.minS:
            return self.minS[-1]
        else:
            return None


if __name__ == '__main__':
    ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
    [[], [-2], [0], [-3], [], [], [], []]
    x = [-2, 0, -3]
    obj = MinStack()
    obj.push(x)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
    print('The result is:', param_3)
    print('The result is:', param_4)