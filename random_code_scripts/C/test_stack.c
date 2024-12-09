#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

bool upordown(int *outer)
{
  int x;
  if (!outer)
  {
    return upordown(&x);
  }
  else
  {
    return &x > outer;
  }
}

int main(int argc, char *argv[])
{
  printf("the stack frames are growing %s\n", upordown(NULL) ? "UP" : "DOWN");
  return EXIT_SUCCESS;
}
