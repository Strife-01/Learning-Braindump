// goroutines are threads managed by the go runtime
go f(x,y,z) // starts the f goroutine

// goroutines run in the same memory space so we need to syncronize data so we don't have race conditions
// sync package provides useful primitives
