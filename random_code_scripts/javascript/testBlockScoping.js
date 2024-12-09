var a = 10;

{
  let a = 100;
  console.log(a);
}

console.log(a);


let b = 10;

function fn() {
  var b = 100;
  console.log(b);
}

fn();
console.log(b);
