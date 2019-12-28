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
# 循环类
"The below is foreach loop:"
$var=1,2,3,4,5,6
foreach($i in $var)  # foreach循环
{
    $n++
    Write-Host "$i"
}
Write-Host "there were $n record"
# 直接获取管道数据
$n=0
"a","b","c","d"|foreach{
    $n++
    Write-Host $_
}
Write-Host "there were $n record"
# while 循环
"The below is while loop: "
$n = 0
while($n -le5) # 当$n小于等于5时，执行下面的操作
{
    Write-Host $n
    $n++
}
# do while的用法
"The below is do while loop:"
$n = 0
do
{
    Write-Host $n
    $n++
}
while($n -ne 3) # 当n不等于3时进行循环操作
# do...until的用法
"The below is do until loop"
$n = 0
do
{
    Write-Host $n
    $n++
}
until($n -gt3) #当$n大于3时停止操作
# if的用法
# Get-Service | foreach {
#     if($_status -eq "running"){
#         Write-Host $_.DisplayName "("$_status")" -ForegroundColor "green"
#     }
#     else {
#         Write-Host $_.DisplayName "("$_status")" -ForegroundColor "red"
#     }
}
