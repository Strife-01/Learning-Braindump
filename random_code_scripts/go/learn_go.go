package main
import ("fmt")

func main() {
  // array
  var student = [50]uint8{};
  // arrays are zeroed by default
  fmt.Println(student)
  for i := 0; i < cap(student); i++ {
    student[i] = (uint8) (i);
  }

  // slice
  new_student := student[4:5]


  slice := []int{1,2,3}
  

  // capacity default = length
  // use the make([]type, length, capacity) function
  // it fills them with 0
  new_slice := make([]float32, 10, 30)
  fmt.Println(new_slice)

  // add items to a slice using append(slice_name, values,separated,by,commas)
  array := [10]int{}
  //array = append(array, 12) cannot append to arrays
  sl := []string{}
  sl = append(sl, "hello") // can append to slices
  var inferred_length_array = [...]uint8{} // [...] the length is inferred


  var slice_1 = []string{"str1", "str2"}
  var slice_2 = []string{"str3", "str4"}
  // append from one slice through destructing - in the opposit direction as in js/ts\
  slice_1 = append(slice_1, slice_2...)
  fmt.Println(slice_1)
  fmt.Println(slice_2)


  // The slice appending works by go creating an array with all the elements and storring them in memory
  // To use less memory and make everything more efficient we can use the function copy()
  // copy will allocate space only for the elements that need to be copied
  // it takes 2 slices and returns the number of elements that the 2nd slice overrides from slice 1 from index 0 onwards
  // this is because the function copies the elements from slice 2 into slice 1
  // good for copies
  

  var slice_3 = []int{1,2,3,4,5}
  var slice_4 = []int{4,5,6}

  fmt.Println(copy(slice_3, slice_4))
  fmt.Println(slice_3)
  fmt.Println(slice_4)


  fmt.Println(array)
  fmt.Println(sl)
  fmt.Println(inferred_length_array)
  fmt.Println(new_student);
  fmt.Println(cap(new_student));
  fmt.Println(cap(student));
  fmt.Println(cap(slice));
  fmt.Println(len(slice));

  
  // Operators:
  /*
  * + - addition/concatenation
  * - - subtraction
  * * - multiplication
  * / - division
  * % - modulo
  * ++ - increment
  * -- - decrement
  *
  // assignment opperators
  * = assignment
  * := assignment
  * +=
  * -=
  * *=
  * %=
  * &=
  * |=
  * ^=
  * >>=
  * <<=
  *
  // Comparison operators
  * ==
  * !=
  * >
  * <
  * >=
  * <=
  *
  // Logical operators
  // !
  // &&
  // ||
  //
  // Bitwise operators
  // &
  // |
  // ^
  // >>
  // <<
  //
  // () presidence
  // (type) (variable) = force casting
  */

  if 10 == 10 {
    // do somethig
  } else {
    // do something else
  }

  if "condition" == "condition" {

  } else if "another condition" != "another_condition" {

  } else {

  }

  //var control int = 10;
  //var controlled int = control == 10 ? 5 : 7; golang doesn't have ternary opperators
/*
  switch expression {
  case condition, multi_case:
    // doesn't need break statement
    
  }
default: 
*/

  // in go you have only for loops but you can make a while with a for loop
  //for starting_condition; keeping_condition; incremental_condition {

  // break continue
  // in go you have the .enumerate() in python by default
  for index, value := range array { // | slice | map
    fmt.Println(index, value)
  }
  // _ pythonic underscore for unwanted values 
  //go func() {
    // IIFEs in go
  //}()

  // const CONSTANT int = 12;
  //
  var greeting = myFunct;
  greeting()

  var add_5 = addTwo(5)
  fmt.Println(add_5(50))


  fmt.Println(add_multiple(1))
  fmt.Println(add_multiple(1,2,3,4,5,6,7))
}
// declare functions func function_name (parameters type ) return type {} 
  func myFunct() {
    fmt.Println("hello")
  }
  // the functions can be closures
  // functions are first class functions so they can be assigned to the variables
  // go has currying
  func addTwo(a int) func(b int) int {
    return func(b int) int {
      return a + b
    }
  }

  // destructing for arguments
  func add_multiple (a... int) int {
    var sum int = 0
    for _, value := range a {
      sum += value
    }
    return sum
  }

  // go has multiple returns return a, b; and we can destruct the return; it pushes multiple values to the stack

  // you can specify the declaration of the return values in the return type 
  func return_2 () (va1 int, va2 string) {
    va1 = 21
    va2 = "hellp"
    return;
  }

  // have reccursion
  type car struct {
    manufacturing_year int;
    manufacturer string;
  }
  // null == nil
  // Go has generics but you have to specify type constraints or any for any type
  func print_something [V any] (value V) {
    fmt.Println(value)
  }



  // maps are nil by default and store reference types
  // len() gets you the length
  // map[keyType]valueType{key:value, }
  var a = map[string]int{key:value}

  // can use make also for map creation
  // var m = make(map[keyType]valueType)
  // m[key] = value
  //
  //
  // Interfaces in go 
  // remove elements from mak delete(map_name, key )
  //
  // can check if a certain value exist in a map by
  // val, ok := map[key] ok is a boolean value
  //for k, v := range a {

  //}

  // pointers are like in C but there is no pointer arithmatic
  //var x *T;
  // default is nil
  // &x reference x *x dereference x 
