#include <stdio.h>
#include <stdlib.h>

int prod_div (int n);

FILE *p_in;
FILE *p_out;

int x, y, prod_div_x, prod_div_y;
char line_in[128];

int main(int argc, char *argv[])
{
    char *file_in, *file_out;

    if (argc != 3)
    {
        printf("Usage: ./program file_in file_out\n");
        return 1;
    }

    file_in = argv[1];
    file_out = argv[2];

    p_in = fopen(file_in, "r");
    if (p_in == NULL)
    {
        printf("Can't open %s\n", file_in);
        return 2;
    }

    p_out = fopen(file_out, "w");
    if (p_out == NULL)
    {
        printf("Can't open %s\n", file_out);
        return 2;
    }

    fgets(line_in, sizeof(line_in), p_in);

    if (sscanf(line_in, "%i %i", &x, &y) != 2)
    {
        printf("You need 2 numbers for this exercise.\n");
        return 3;
    }

    prod_div_x = prod_div(x);
    prod_div_y = prod_div(y);

    if (prod_div_x > prod_div_y)
    {
        fprintf(p_out, "%i\n", prod_div_x);
    }
    else if (prod_div_y > prod_div_x)
    {
        fprintf(p_out, "%i\n", prod_div_y);
    }
    else
    {
        if (x > y)
        {
            fprintf(p_out, "%i\n", y);
        }
        else
        {
            fprintf(p_out, "%i\n", x);
        }
    }
    

    fclose(p_in);
    fclose(p_out);

    return 0;
}

int prod_div (int n)
{
    int prod = 1;

    for (int i = 2; i <= n; i++)
    {
        if (n % i == 0)
        {
            prod *= i;
            while (n % i == 0)
            {
                n /= i;
            }
        }
    }

    return prod;
}
