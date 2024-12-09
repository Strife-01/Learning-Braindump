#include "./read_from_file.h"

int main(int argc, char *argv[])
{
  print();
  FILE *file = fopen(argv[1], "r");
  char string[100];

  while (fgets(string, 100, file)) {
    printf("%s", string);
  }

  return 0;
}
