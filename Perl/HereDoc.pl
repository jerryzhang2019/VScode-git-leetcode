$a = 10;
$var = <<"EOF";
This is an example of here DOC，using double。
可以在这输入字符串和变量。
例如： a = $a
EOF
print "$var\n";

$var = <<'EOF';
这是一个here文档实例，使用单引号。
例如：a = $a
EOF
print "$var\n"