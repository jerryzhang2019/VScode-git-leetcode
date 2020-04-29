var result= ((3!=6%3)&&!(24>45)&&(!false));
console.log(result)

for(var i =0; i<6; i = i +1){
    console.log("Printing out i = " + i);
}

for (var x = 0; x < 5; x = x + 1) {
    for (var y = 0; y < 3; y = y + 1) {
      console.log(x + "," + y);
    }
  }

  for (var i = 0; i <= 6; i = i + 2) {
    console.log(i);
  }

  sayHi("Julia");

function sayHi(name) {
  console.log(greeting + " " + name);
  var greeting;
}

sayHi("Julia");

function sayHi(name) {
  console.log(greeting + " " + name);
  var greeting = "Hello";
}