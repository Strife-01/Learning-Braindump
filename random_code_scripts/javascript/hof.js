arr = [5, 1, 3, 2, 6];

// Map

const double = arr.map((item) => item * 2);
const triple = arr.map((item) => item * 3);
const binary = arr.map((item) => {
  let b = 0;
  let p = 1;
  let c_item = item;
  while (c_item != 0) {
    b = b + c_item % 2 * p;
    p *= 10;
    c_item /= 2;
    c_item = Math.floor(c_item);
  }
  return b;
})

console.log("Map Execution");
console.log(double, triple, binary);

// Filter

const odd = arr.filter((item) => item % 2 === 1);
const even = arr.filter((item) => item % 2 === 0);

console.log("Filter Execution");
console.log(odd, even);

// Reduce

const sum = arr.reduce((previous, current) => previous + current, 0);
const max = arr.reduce((previous, current) => current > previous ? current : previous, arr[0])

console.log("Reduce Execution");
console.log(sum, max);

const users = [
  {firstName: "Andrei", lastName: "Ursachi", age: 23},
  {firstName: "Adrian", lastName: "Ursachi", age: 49},
  {firstName: "Mariana", lastName: "Ursachi", age: 49},
  {firstName: "Mihai", lastName: "Ursachi", age: 16},
  {firstName: "Anghelina", lastName: "Rata", age: 20},
];

const users_list = users.map((user) => `${user.firstName} ${user.lastName}`);
const nr_seniors = users.reduce((acc, user) => user.age >= 23 ? ++acc : acc, 0);
const age_groups = users.reduce((acc, user) => { 
  acc[user.age] ? acc[user.age]++ : acc[user.age] = 1
  return acc;
}, {})
const less_than_30 = users.filter((user) => user.age < 30)
                          .map((user) => user.firstName);

const less_than_30_reduce = users.reduce((acc, user) => {
  if (user.age < 30) {
    acc.push(user.firstName);
  }
  return acc;
}, []);

console.log(users_list, nr_seniors);
console.log(age_groups);
console.log(less_than_30);
console.log(less_than_30_reduce);
