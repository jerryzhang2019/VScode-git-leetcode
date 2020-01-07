# 准确查找IP地址方法1
# $a = ipconfig.exe
# $a[8]
# $a[10].Substring(39)

# 方法2
$match = @($a | Select-String "IP")
$ipstring = $match[0].line
$ipstring

# 方法3
$index = $ipstring.$indexof(": ")
$ipstring.Substring($index+2)
$ipaddress = [net.ipaddress]$ipstring.Substring($index+2)
$ipaddress

