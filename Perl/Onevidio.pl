 use strict;
 use warnings;
use diagnostics;

#字符串
my $name = "jerry zhang";
my ($age, $street) = (40, '123 Main St');
my $my_info = "$name lives on \"$street\"\n";
$my_info = qq{$name lives on "$street"\n};
print $my_info;

#整段注释
my $bunch_on_info = <<"END";
This is a 
bunch of information
on multiple lines
END
say $bunch_on_info;

#条件分支 if...elseif...else
my $word = "antidisestablishmentarianism";
my $strlen = length $word;

if($strlen >= 15){
    print "'", $word, "' is a very long word";
}elsif(10 <= $strlen && $strlen < 15){
    print "'", $word, "' is a medium-length word";
}else{
    print "'", $word, "' is a short word";
}

#简短语法
print "'", $word, "' is acctually enormous" if $strlen >= 20;

