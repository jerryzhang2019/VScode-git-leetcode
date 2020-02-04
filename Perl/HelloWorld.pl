print "Hello World\n"; # 双引号
print 'Hello World\n'; # 单引号

=pod
输出结果：
Hello World
Hello World\n
结论：Perl双引号和单引号的区别: 双引号可以正常解析一些转义字符与变量，而单引号无法解析会原样输出。
=cut

# perl 也支持多行注释，最常用的方法是使用 POD(Plain Old Documentations) 来进行多行注释。
=pod 注释
这是一个多行注释
这是一个多行注释
这是一个多行注释
这是一个多行注释
=cut

# 单引号和双引号的另外的一个例子：
$a = 10;
print "a = $a\n";
print 'a = $a\n';

=pod
EOF在这里通俗讲就是一个标记，他用来标记一段文字（一般都是多行的，省得编码麻烦，用"<<"加上一个标记就可以把一大段代码存入到一个变量中去了）
$a=<< “EOF” 的意思就是说：下一行开始，直到遇见“EOF”为止，所有的字符都按照指定的格式存入变量a中。
你可以用EEE，MAMA等等其他的名字都可以，就是一个标记而已。他的作用就是简化输入。
=cut

