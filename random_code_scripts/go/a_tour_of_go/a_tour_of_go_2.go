// in go the io is implemented with io.Reader interface which reads streams of data 1 byte at a time
// there are many implementations of the std library
// files, network connection, compressors, ciphers, etc
// io.Reader Read method
// func (T) Read(b []byte) (n int, err error) {}
// returns the number of bytes it populated and an io.EOF error when it finished reading
//
package main

import "golang.org/x/tour/reader"

type MyReader struct{}

func (reader MyReader) Read(buffer []byte) (int, error) {
	for i, _ := range buffer {
		buffer[i] = 'A'
	}
	return len(buffer), nil
}

func main() {
	reader.Validate(MyReader{})
}


package main

import (
	"io"
	"os"
	"strings"
	"fmt"
)

type rot13Reader struct {
	r io.Reader
}

func (r rot13Reader) Read(buffer []byte) (int, error) {
	n, err := r.r.Read(buffer) // Read from the underlying reader
	if err != nil && err.Error() != "EOF" {
		return n, err
	}

	for i := 0; i < n; i++ {
		chr := buffer[i]
		// Apply ROT13 to uppercase letters (A-Z)
		if chr >= 'A' && chr <= 'Z' {
			buffer[i] = (chr-'A'+13)%26 + 'A'
		} 
		// Apply ROT13 to lowercase letters (a-z)
		if chr >= 'a' && chr <= 'z' {
			buffer[i] = (chr-'a'+13)%26 + 'a'
		}
	}
	return n, err
}

func main() {
	s := strings.NewReader("Lbh penpxrq gur pbqr!")
	r := rot13Reader{s}
	io.Copy(os.Stdout, &r)
}

Images

Package image defines the Image interface:

package image

type Image interface {
    ColorModel() color.Model
    Bounds() Rectangle
    At(x, y int) color.Color
}

Note: the Rectangle return value of the Bounds method is actually an image.Rectangle, as the declaration is inside package image.

(See the documentation for all the details.)

//The color.Color and color.Model types are also interfaces, but we'll ignore that by using the predefined implementations color.RGBA and color.RGBAModel. These interfaces and types are specified by the image/color package



func Index[T comparable](s []T, x T) int
generic types can be parameterized
