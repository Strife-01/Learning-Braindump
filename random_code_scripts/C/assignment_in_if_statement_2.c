#include <stdio.h>

#define EXIT_SUCCESS 0
#define true 1
#define false 0

int retrival (char status)
{
  return status;
}

int main(int argc, char *argv[])
{
  char test;

  {
    printf("%s\n", "hello");
  }

  if ((test = retrival(false)))
  {
    printf("%s\n", "success");
  }
  else 
  {
    printf("%s\n", "failure");
  }

  if (true) printf("%s\n", "wow you can really do this");

  return EXIT_SUCCESS;
}
