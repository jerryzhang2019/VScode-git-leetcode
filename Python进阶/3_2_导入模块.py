# 导入模块 或者调用别的文件
import math
print(math.pow(2, 0.5))  # pow是函数
print(math.pi)  # pi是变量
from math import pow, sin, log  # 从模块中导入某个函数，而不是全部
print(pow(2, 10))
print(sin(3.14))
# 如何解决重名的问题？
import math, logging
print(math.log(10))
logging.log(10, 'something')

from math import log
from logging import log as logger
print(log(10))
logger(10, 'import from logging')
