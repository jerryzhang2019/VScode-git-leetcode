# 转换整型 ‘/’除会得到浮点数；而'//'除才会得到整数。
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __init__(self):
        return self.p // self.q  # 转换整形的方法 //符号表示取整操作

    def __float__(self):
        return float(self.p) / self.q  # 转换浮点型的方法 /符号表示除法运算

if __name__ == '__main__':
    result1 = int(Rational(7, 2))
    result2 = int(Rational(1, 3))
    print(result1, result2)