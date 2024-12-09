function Counter() {
  this.logCounter = function () {
    console.log(count);
  }
  this.increaseCount = function () {
    count++;
    this.logCounter();
  }
  this.decreaseCount = function () {
    count--;
    this.logCounter();
  }
  let count = 0;
}

let counter = new Counter();
for (let index = 0; index < 2; index++) {
  counter.increaseCount();
}

counter.decreaseCount();
