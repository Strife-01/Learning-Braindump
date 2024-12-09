function addTwo(add) {
  return function (a) {
    return function (b) {
      return add(a, b)
    }
  }
}

function add(a, b) {
  return a + b
}

let add_5 = addTwo(add)(5)
let added = addTwo(add)(5)(2)
console.log(add_5(5))
console.log(added)
