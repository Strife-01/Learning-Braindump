#include <stdio.h>

// static variables that are cleared from static memory after the process finishes
static int a = 0;
static int b = 1;

// the function generator we point to
int fib()
{
    int result = a;
    a = b;
    b = a + b;
    return result;
}

// a function pointer with no parameters that returns a function that returns an int
int (*fibonacci()) ()
{
    return &fib;
}

int main()
{
    for (int i = 0; i < 10; i++)
    {
        // A kind of first class function
        // It uses the address of the function in the Code segment in memory
        // Assgines to a function pointer the address of fib function returned by fibonacci
        int (*fibo)() = fibonacci();
        // this uses function currying in C
        printf("%i'th element in the fibonacci sequence is %i.\n", i + 1, fibo());    
    }

}
