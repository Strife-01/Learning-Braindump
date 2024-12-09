#include <stdio.h>

#define EXIT_SUCCESS 0

int main(int argc, char *argv[])
{
  void fun(void) 
  {
    printf("%s\n", "Hello");
  }

  fun();
  return EXIT_SUCCESS;
}
