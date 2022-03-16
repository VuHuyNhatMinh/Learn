#include <stdio.h>

int main()
{
    unsigned short n;
    scanf("%hu", &n);
    unsigned int max;
    scanf("%u", &max);

    unsigned int res = 0;
    for (int i = 1 ; i < n ; i = i + 1)
    {
        unsigned int a;
        scanf("%u", &a);
        if (a < max)
        {
            res = res + (max - a);
        }
        else if (a > max)
        {
            res = res + (a - max) * i;
            max = a;
        }
    }

    printf("%u\n", res);
    return 0;
}