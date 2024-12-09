function sum() {
  let sum = 0;
  for (let index = 0; index < this.length; index++) {
    sum += this[index];
  }
  return sum;
}

Array.prototype.sum = sum;

function r(...args) {
  console.log(args.sum());
  console.log([...args]);
  
}

r(1, 2, 4);


