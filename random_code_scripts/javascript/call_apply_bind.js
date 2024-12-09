let obj1 = {
  name: "Andrei",
  //printName: function () {
  //  console.log(this.name);
  //},
}

let printName = function () {
  console.log(this.name);
}

let printData = function (homeTown) {
  console.log(`${this.name} from ${homeTown}`);
}

let obj2 = {
  name: "Anghelina",
}

printName.call(obj1); // function borrowing
printData.call(obj2, "Izvoare");
printData.apply(obj2, ["Izvoare"]);

const print_data = printData.bind(obj1, "Iasi");
print_data();
