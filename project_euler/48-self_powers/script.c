#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <float.h>

// UNFINISHED

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("This program requires a single extra command line argument.\n");
        return -1;
    }

    double sum = 0;
    int limit = atoi(argv[1]);

    for (int i = 1; i <= limit; i++)
    {
        sum += pow(i, i);
    }
    printf("%f\n", sum);
    return 0;
}