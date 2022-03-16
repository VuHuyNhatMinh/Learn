#include <stdio.h>

int main(void)
{
    unsigned int x;
    scanf("%u", &x);

    unsigned int res = 1;
    while (x != 1)
    {
        if (x % 2 == 1)
        {
            x = x - 1;
            res = res + 1;
        }
        else if (x % 2 == 0)
        {
            x = x / 2;
        }
    }

    printf("%u\n", res);
}