#include <stdio.h>
#include <stdlib.h>

#define EXIT_SUCCESS 0
#define EXIT_FAILURE 1

typedef struct{
  int real, imaginary;
} complex;

int main(int argc, char *argv[])
{
  complex *x = malloc(sizeof(complex));
  complex *y = malloc(sizeof(complex));
  
  if (argc <= 4)
  {
    exit(EXIT_FAILURE);
  }

  x->real = (int) atoi (argv[1]);
  x->imaginary = (int) atoi (argv[2]);
  y->real = (int) atoi (argv[3]);
  y->imaginary = (int) atoi (argv[4]);
  
  int real_result = x->real * y->real - x->imaginary * y->imaginary;
  int imaginary_result = x->real * y->imaginary + x->imaginary * y->real;

  printf("%i %ii\n", real_result, imaginary_result);

  free(x);
  free(y);

  return EXIT_SUCCESS;
}
