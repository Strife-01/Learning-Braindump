#include <stdio.h>

int main(void)
{
    int x;
    //scanf("%i", &x);

    x = 11;
    int y = 11;

    if (x++ == 12)
    {
        printf("True\n");
    }
    else
    {
        printf("False\n");
    }

    if (++y == 12)
    {
        printf("True\n");
    }
    else
    {
        printf("False\n");
    }

    int test;
    int test_case_1 = 1;
    int test_case_2 = 0;

    if ((test = test_case_1))
    {
        printf("True\n");
    }
    else
    {
        printf("False\n");
    }

    if ((test = test_case_2))
    {
        printf("True\n");
    }
    else
    {
        printf("False\n");
    }

    return 0;
}
