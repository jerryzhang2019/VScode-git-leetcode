var laugh = function laugh(num){
    var x=1;
    var result="";
    while(x<=num){
        result +="ha";
        num--;
    }
    return result+"!";

}

console.log(laugh(3));