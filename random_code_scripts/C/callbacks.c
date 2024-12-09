#include <assert.h>
#include <errno.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define EXIT_SUCCESS 0

enum ERROR
{
  NOT_ENOUGH_CLA = 1,
};

char * get_message (char * message)
{
  return message;
}

void print(char * m, char* (*message) (char *))
{
  printf("%s\n", message(m));
}

int main(int argc, char *argv[])
{
  char *keyboard_message = malloc(20 * sizeof(char));

  if (argc < 2)
  {
    print("Usage: ./callbacks 'message'", get_message);
    return NOT_ENOUGH_CLA;
  }

  print("What text you wanna print? ", get_message);
  scanf("%[^\n]s", keyboard_message);
  print(keyboard_message, get_message);
  
  print(argv[1], get_message);

  free(keyboard_message);

  return EXIT_SUCCESS;
}
