function greet (name: string, date: Date) {
  console.log(`Hello ${name}, today is ${date.toDateString()}!`);
}

greet("Andrei", new Date());

function test (): number {
  return 22;
}

console.log(test());


//export async function as (name: string): Promise<string> {
//  return name;
//}

// let x = await as("Andrei");

//console.log(x);

const names = ["Andrei", "Anghelina"];

names.forEach((e) => {
  console.log(e);
});

function test_obj (obj_name: {first: string, last?: string}) {
  // method 1
  console.log(obj_name.first);

  if (obj_name.last !== undefined) {
    console.log(obj_name.last);
  }

  // Method 2
  console.log(obj_name.last?.toLowerCase());
}

test_obj({first: "andrei", last: "anghelina"});
test_obj({first: "andrei"});

function union_test (id: number | string) {
  console.log(id);
}

union_test("100");
union_test(100);
//union_test({id: 100});


// working with Unions and Array types
function union_test_2 (ar: string[] | string) {
  if (Array.isArray(ar)) {
    console.log(`Hello ${ar.join(" and ")}`);
  }
  else {
    console.log(`Hello ${ar}`);
  }
}

union_test_2(["Andrei", "Anghelina"]);
union_test_2("Andrei");
//union_test_2([2]);


//Working with type aliases I.E. Create a special data type to use ~ typedef

type Point = {
  x: number,
  y: number
}

function coord(pt: Point) {
  console.log(`The point is located at x = ${pt.x}, y = ${pt.y}`);
}

coord({x: -1, y: 2});

type ID = number | string;
let id_1: ID = "1";
let id_2: ID = 1;
// let id_3: ID = {id: 1};

// Using interfaces in typescript vs using type - interface allows you to add new fields but the type does not

// Create an interface
interface Point_2d {
  x: number;
  y: number;
}

let p1: Point_2d;
p1 = {x: 1, y: 2, name: "Andrei"};

console.log(p1);

// Adding functionality to an interface
interface Point_2d {
  name: string;
}

// Extending an interface
//interface Point_3d extends Point_2d {
//  z: number;
//}

//let p2: Point_3d = {x: 1, y:2, z: 3};
//console.log(p2);


type Animal = {
  name: string;
}

let x: Animal = {name: "lion"};
console.log(x);

// extend a type in typescript
type Bear = Animal & {
  honey: boolean;
}

let bear: Bear = {name: "bear", honey: true};
console.log(bear);

// a type cannot be changed after creation

// when you need a more specific type that typescript doesn't know about you can use type assertion
// const canvas = document.getElementById("main_canvas") as myHTMLCanvas;
// If you are not using a .tsx file you can also use the syntax below with bracket notation - same shit
// const canvas = <myHTMLCanvas>document.getElementById("myCanvas");


const v = "12" as "string";
// const v: string = "12";
console.log(v);

const xz = "hello" as any as "hello";
console.log(xz);

// Value bounding - literal types
let names_1: "names" = "names";

// This cannot happen
//names_1 = "Andrei";
//names_1 = "Anghelina";
//names_1 = "James";

// Use value bounding in useful situations to bound the user into using specific values
function test_literal_types (s: string, position: "up" | "down" | "left" | "right" | "center") {
  console.log(`${s} is ${position}`);
}

test_literal_types ("Andrei", "center");
//test_literal_types ("Andrei", "Andrei");

// you can use literal return types to bound a function to return specific values
function literal_return_test (a:string, b:string): -1 | 0 | 1 {
  return a === b ? 0: a > b ? 1 : -1;
}

// you can use literal types with types and you can combine different literals and different types
// there is also the boolean type which has 2 literal types true or false and boolean is just a type for the union true | false

// the declare keyword is used in typescript to specify that the specific variable object or function is already created somewhere else and the complier doesn't need to create any js for it, it can just reference it where it is declared



