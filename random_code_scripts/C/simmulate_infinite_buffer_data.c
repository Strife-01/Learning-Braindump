#include <stdio.h>
#include <stdlib.h>

// length_array = sizeof(array) / sizeof(array[0])
// works only if array is an array
// if array is a pointer malloced, it won't work as it will return the size of the pointer which is 8 bytes
// or sizeof(*pointer) will return the size of the element if the *(pointer + 0)

int main(void)
{
	int *vector = malloc(sizeof(int));
	if (vector == NULL)
	{
		printf("Fail - code 1\n");
		return 1;
	}

	int length = 0;
	int buffer;

	printf("Dinamically read a vector in memory:\n");
	while(scanf("%i", &buffer) && buffer)
	{
    int* temp = realloc(vector,  (length + 1) * sizeof(int));
    
    if (temp == NULL)
		{
			printf("Fail - code 2\n");
      free(vector);
			return 2;
		}
    
    if (temp != vector)
    {
      printf("Memory moved\nFree old memory\n");
      vector = temp;
    }

    vector[length++] = buffer;
	}

	printf("--- Dinamically get the length of the vector ---\n");
	printf("Bytes in vector: %lu\n", sizeof(*vector) * length);
	printf("Length of vector: %i\n", length);

	int index = 0;
	while(index < length)
	{
		printf("%i ", vector[index++]);
	}
	printf("\n");

	free(vector);
}
