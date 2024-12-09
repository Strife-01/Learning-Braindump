package main;

import (
  "fmt";
)

func updown [T any] (value *T) bool {
  var x T;
  if value == nil {
    return updown(&x);
  }
  // Go doesn't have pointer arithmatic so this doesn't work - it makes it safer but still shame
  return &x > value;
}

func main() {
  fmt.Println(updown(nil));
}
