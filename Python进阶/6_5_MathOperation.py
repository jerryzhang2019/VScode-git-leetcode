# 数学中的加减乘除
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __add__(self, r):
        return Rational(self.p*r.q + self.q*r.p, self.q * r.q)  # 通分运算
#  self是其中一个分数,r是另外一个分数,则分数计算法则[(s（self）的分子*r的分母 +s的分母 * r的分子)]—>
# （整个就是结果的分子）,(s的分母*r的分母)—>(整个就是结果的分母)
    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)
    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)
    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):
        g = gcd(self.p/g, self.q)
        return '%s/%s' % (self.p, self.q)
    __repr__ = __str__

r1 = Rational(1, 2)
r2 = Rational(1, 4)
print(r1 + r2)
print(r1 - r2)
print(r1 * r2)
print(r1 / r2)