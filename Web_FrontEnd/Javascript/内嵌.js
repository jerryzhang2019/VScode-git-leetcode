function emotions(myString, myFunc){
    console.log("I am "+ myString + "," + myFunc(2));
}

emotions("happy",function(num){
    var x=1;
    var result="";
    while(x<=num){
        result +="ha";
        num--;
    }
    return result+"!";
})
