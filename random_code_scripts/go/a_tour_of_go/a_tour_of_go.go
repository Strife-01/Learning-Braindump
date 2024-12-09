package main

import (
  "fmt";
  "time";
//  "math";
//  "math/rand";
    "strconv";
)

// non innitialized variables are defaulted to zeros
// typecasting: variable T = T(v)        %T formats the type
// constants const
// constants can be factored and if we don't specify the type they inferr it from the assignment

// var declarations can be factored as import can
var (
  x complex128 = 10 - 1i;
  y uint32 = 398234;
)

func main() {
  fmt.Println(time.Now());
  fmt.Println(naked_function(1,2));
  fmt.Println(x, y)
}

func naked_function(arg1, arg2 int) (sum_args int) {
  sum_args = arg1 + arg2;
  {
    //x := sum_args;
    //fmt.Println(x);
  }
  return;
}

// can multiple innitialize
//var v1, v2 int = 1, 2;
// in innitialize type can be inferred
// := can be used inside a function
//

// in for the init and post conditions are optional but the condition is required
// if we use for with only the condition then we get a while loop
// switch {}  the same as switch true {}

// defer - will exectue the expression just untill the function in which it is used returns - it will push back everything until return
// defer pushes the execution to the stack so
/*
for i := 0; i < 10; i++ {
  defer fmt.Println(i);
}
*/
// will print 9 8 7 ... 0 as they are pushed lifo 

//
//go does have pointers as references to addresses but it doesn't have pointer arithmatic

type Car struct {
  manufacturer string;
  year int;
}

var ford = Car{"Ford", 2010};
// acces with pointer to the struct 
// (*ford).year
// can write directly ford.year
// you can have pointers to struct types &Car will get type *Car
//
// in declareation we can innitialize only the fields we want with the name: value syntax - the other ones will be zeroed

// array [n]T
// len()
// make()
// cap()
// slices a[i:up_but_not_including] - are dynamic
//
// so slices are references to underlying arrays so every array that that is referenced by the slice will see the changes a slice makes to an array
//
// copy()
//
// a slice literal is an array literal without a length a[:]
//
// the length of the slice are the number of elements in in
// the cappacity are the elements in the underlying array starting from the very first element of the array
//
// range keyword
// range retuns the current index and the value at that index
// _ to skip a value
//
// the default for a slice is nil = length == capacity == 0 and no underlying array
//
// make (slice, length, capacity)
// slices can contain any type and other slices but they have to have 1 type
//
//
// if the underlying array is too small for adding new values then a new array is allocated and the pointer to the new array is returned
// append(slice []T, secondslice ...T)
// func append(s []T, vs ...T) []T; - we need to capture the append into the new old slice 
//
//
// map[type]type   -   key: value
//
// make (map[type]type)
// maps are nil by default 
//
// map literals are like struct literals but they are key required
//
//
// m[key] = assignment
// retrieval = m[key]
// delete(map, key)
// elem, ok = map[key]
// ok boolean checks the existance of the elem
// elem is the value of the key or the zero form of that type

// functions are first class functions and they can be passed returned curried clorured etc also has IIFEs and lambda expressions
// type is used to create a new type of any sorts


// Go doesn't have classes but it has methods on types
// it works for any type created with the type keyword. not just structs
// you can only declare receivers with the types delcared in the same package
// so no primitive types, but you can typedef them and you will make them fine
// in go a method is just a function with a receiver argument
type Vertex struct {
  X float64;
  Y float64;
}

//(&v).X or v.X

// you can have pointer types for receivers. the pointer receivers will allow you to modify the underlying value as it will be passed by reference not by value

// func receiver_argument for the type name_of_funciton and return type
func (v Vertex) Abs() float64 {
  //
}

var v Vertex = {10, 12.5}
v.Abs()


// an interface is a set of method signatures 
type Abaser interface {
  Abs() float64;
}

// we can declare something to be of an interface type if they hold as value the return type of one of the implemented funcitons 
// we don't need to implement and interface as it implements itself
// a type implements an interface by implementing its methods
//
// under the hood an interface value can be taught as a tuple (value, type)
//
// interfaces are used to specify what behaviour a type should have like in Java
// but it is not just for methods

//so you specify all the methods or functions that are associated with a certain type that we declare
//if the concrete value that the interface is applied to is nil we should gracefully deal with it
// the interface is nil but if the concrete value is nil than the interface is not nil as it has a concrete value
// a nil interface doesn't have a value or a concrete value will throw a runtime exception
package main

import "fmt"

type I interface {
	M()
}

type T int;

func (t T) M() {
	fmt.Println("this solves it")
}

func main() {
	var i I = T (2)
	describe(i)
	i.M()
}

func describe(i I) {
	fmt.Printf("(%v, %T)\n", i, i)
}


// the empty interface interface{} is used for when you have a variable of an unknow type. eg Print 
//
//We can test an interface concrete underlying value's type by type assertion

t := i.(T)
t, ok := i.(T)

// it will trigger a panic if we access a type that is not the correct type but the one with 2 variables work as it will give a bool

package main

import "fmt"

func main() {
	var i interface{}
	describe(i)

	i = 42
	describe(i)

	i = "hello"
	describe(i)
}

func describe(i interface{}) {
	fmt.Printf("(%v, %T)\n", i, i)
}



type Stringer interface {
  String() string
}

func (t T) String() string {
  return fmt.Sprintf(" ... ", t.Field1)
}

// Now if we create a type T when we print a value of type t we will print the returned value of this String() function
// kinda like overriding a method 
// used in fmt and not only like .toString() in java or __str__ in python:wq
// Sprintf waits for an interface of type any so it won't work like this
//
//
// the errors are represented with error values 
// error type is an interface built in like fmt.Stringer

type error interface {
  Error() string
}

//fmt package looks for the Stringer and for the error when printing values
// functions usually return also an error to signal if we have an error or not. because it is an interface if we have no error the interface has no
// underlying value or concrete value so it is nil
// we use it to check for errors 
// use like exceptions in Java
i, err := strconv.Atoi("42")
if err != nil {
  fmt.Println(err)
  return 
}




package main

import (
	"errors"
	"fmt"
)

// Method 1: Using errors.New()
func method1() error {
	return errors.New("this is a new error")
}

// Method 2: Creating a custom error type that implements the error interface
type MyCustomError struct {
	message string
}

func (e MyCustomError) Error() string {
	return e.message
}

func method2() error {
	return MyCustomError{"this is a custom error"}
}

// Method 3: Type conversion (what you asked about)
func method3() error {
	customErr := MyCustomError{"conversion error"}
	return error(customErr)  // Explicit type conversion
}

func main() {
	// All of these work because they satisfy the error interface
	fmt.Println(method1())
	fmt.Println(method2())
	fmt.Println(method3())
}

