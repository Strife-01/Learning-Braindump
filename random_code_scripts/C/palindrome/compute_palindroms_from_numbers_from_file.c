#include <stdio.h>
#include <stdlib.h>

#define nr_files 3
#define max_file_read 10000

#define true 1
#define false 0

typedef char* string;

int is_palin (int n);
int is_prim (int n);

FILE * d_in;
FILE * d_out;

char line[max_file_read];
string file_in, file_out;

int nr_n, x;

int main (int argc, string argv[])
{
    if (argc != nr_files)
    {
        printf("Usage: ./t2 file_in file_out\n");
        return 1;
    }

    file_in = argv[1];
    file_out = argv[2];

    d_in = fopen (file_in, "r");
    if (d_in == NULL)
    {
        printf("Can't open %s\n", file_in);
        return 2;
    }

    d_out = fopen (file_out, "w");
    if (d_out == NULL)
    {
        printf("Can't open %s\n", file_out);
        return 2;
    }

    fgets (line, sizeof(line), d_in);
    
    sscanf(line, "%i", &nr_n);

    while (nr_n && fgets (line, sizeof(line), d_in))
    {
        sscanf(line, "%i", &x);

        if (is_palin(x) && is_prim(x))
        {
            fprintf(d_out, "%i\n", x);
        }
        nr_n--;
    }

    fclose (d_in);
    fclose (d_out);

    return 0;
}

int is_palin (int n)
{
    int cn = n, palin = 0;

    while (cn)
    {
        palin *= 10;
        palin += cn % 10;
        cn /= 10;
    }

    return (palin == n) ? true : false;
}

int is_prim (int n)
{
    for (int i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            return false;
        }
    }

    return true;
}
