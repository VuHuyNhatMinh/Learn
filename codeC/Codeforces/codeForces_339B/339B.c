#include <stdio.h>

int main(void)
{
    unsigned int n, m;
    scanf("%u%u", &n, &m);

    unsigned long long int res = 0;

    unsigned int pos = 1;
    for (unsigned int i = 0 ; i < m ; i = i + 1)
    {
        unsigned int a;
        scanf("%u", &a);

        if (a >= pos)
        {
            res = res + (a - pos);
        }
        else
        {
            res = res + ((n - pos) + a);
        }
        pos = a;
    }

    printf("%llu\n", res);
}