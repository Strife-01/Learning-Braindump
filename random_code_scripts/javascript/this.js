"use strict"; // works only if use strict is in the beginning of the file

function k() {
  console.log(this); // undefined or global objact dep on strict/nonstrict mode
}

//function t() {
  //this.k(); // undefined or global objact dep on strict/nonstrict mode
//}

k(); // this substitution - global object - non strict mode


//t(); // undefined strict mode

//this.t() // will refferenct the global object

// arrow funcions do not have their own this keyword, only the one of their lexical environment, function statement or object where they are created
// it will not point to the object in which it has been created but to the object in which this object has been created
// where it is enclosed - global object
const y = {

  test_lc: function () {
  

const test_obj = {
  a: 10,
  obj: {
    b: 20,
    // enclosing lexical context
    print: () => {
      console.log(this);
    }
  }
}

test_obj.obj.print();
}
}
y.test_lc();
