console.log("Object Literal approach");

obj = {
  name: "Andrei",
  age: 23,
  getAge: function () {
    console.log(`${this.name}'s age is ${this.age}`);
  }
}

const refFunc = obj.getAge;
const corrRefFunc = refFunc.bind(obj);
corrRefFunc();

console.log("Class approach");

class User {
  constructor (name, age = 0) {
    this.name = name,
    this.age = age
  }

  printUser() {
    console.log(`${this.name}'s age is ${this.age}`);
  }
}

const andrei = new User("Andrei", 23);
const usr = new User("User");

andrei.printUser()
usr.printUser()

const fn = andrei.printUser.bind(andrei)
fn()


