use strict;
use warnings;
use diagnostics;

# 标量
# $myfirst = 123;  # 数字123
# print "my first = $myfirst\n";
# $mysecond = "123";  # 字符串123
# print "my second = $mysecond\n";

my $name = "jerry zhang";
my ($age, $street) = (40, '123 Main St');
my $my_info = "$name lives on \"$street\"\n";
$my_info = qq{$name lives on "$street"\n};
print $my_info;

#空字符
# my $undef = $undef;
# print $undef;

my $undef2;
print $undef2;

my $num = 4040.5;
print $num;

#弱类型
my $str1 = "4G";
my $str2 = "4H";

print $str1. $str2;
print $str1 + $str2;
print $str1 eq $str2;
print $str1 == $str2;

# 数组
# @arr = (1,2,3);
# print "array = @arr\n";
my @array = (
    "print",
    "these",
    "string",
    "out",
    "for",
    "me",
);
print $array[0];
print $array[1];
print $array[2];
print $array[3];
print $array[4];
print $array[5];
print $array[6];

print $array[-1];
print $array[-2];
print $array[-3];
print $array[-4];
print $array[-5];
print $array[-6];
print $array[-7];

# 哈希???没运行出来
# %h = ('a' =>1, 'b' =>2);
# print "h = %h\n";

