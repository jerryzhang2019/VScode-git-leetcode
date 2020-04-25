/*
 * Programming Quiz: Musical Groups (3-3)
 */
/*
 * QUIZ REQUIREMENTS
 * 1. Your code should have a variable `musicians`, and include `if...else if...else` conditional statement
 * 2. Your code should produce the expected output, as mentioned above. Read each condition carefully. 
 */
 
// change the value of `musicians` to test your conditional statements
var musicians = 5;

// your code goes here
if (musicians===1){
    console.log("this is a solo");
}else if(musicians===2){
    console.log("this is a dute");
}else if(musicians===3){
    console.log("this is a trio");
}else if(musicians>=4){
    console.log("this is a larger group");
}else{
    console.log("this is not a group");
}
