#include <stdio.h>

int main(void)
{
    unsigned int a, b;
    scanf("%u%u", &a, &b);

    unsigned int res = a;

    while (1)
    {
        if (a < b)
        {
            break;
        }
        else 
        {
            res = res + a / b;
            a = a / b + a % b;
        }
    }
    printf("%u\n", res);
}