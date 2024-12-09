package main

import (
  "fmt"
)

func adder() func(int) int {
  var sum int = 0
  return func(x int) int {
    sum += x;
    return sum
  }
}

func main() {
  ad := adder();
  fmt.Println(ad(5));
  fmt.Println(adder()(5));
}


/*
package main

import "fmt"

// fibonacci is a function that returns
// a function that returns an int.
func fibonacci() func() int {
	a, b := 0, 1
	return func() int {
		result := a
		a, b = b, a + b
		return result
	}
}

func main() {
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(f())
	}
}
*/
