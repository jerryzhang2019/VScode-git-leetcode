# 数学运算
1+1
2-1
1*2
1/2
# 打印字符串
"Hello World"
# 四则混合运算
(5+23*2)/23
#运算符
1,2,3,5,3,2 -contains 3  # 此数组中是否包含3
1,2,3,5,3,2 -eq 3 # 返回所有等于3的元素
1,2,3,5,3,2 -lt 3 # 返回所有小于3的元素
# if(1,3,5 -contains2): # 测试2是否在集合中
# 类型转换
#(2+2)*3/7 > c:/foo.txt
# 存储到临时变量
$n = (2+2)*3
$n
$n/7
# 运算结果存储到文件
# $files = dir
# $files[ 3]
# 在PowerShell中, 命令分为四类: cmdlet, function, script和native Windows commands.
#get-command -CommandType
#调用运算符
#函数的用法
$var1=10
function one{"The variable is $var1"}
function two{$var1=20;one}
one # The variable is 10
two # The variable is 20
one # The variable is 10
