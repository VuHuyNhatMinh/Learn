#include <stdio.h>

unsigned int min(unsigned int a, unsigned int b)
{
    if (a < b)
    {
        return a;
    }
    else
    {
        return b;
    }
}

int main(void)
{
    unsigned int n, k, l, c, d, p, nl, np;
    scanf("%u %u %u %u %u %u %u %u", &n, &k, &l, &c, &d, &p, &nl, &np);
    unsigned int res = min(k*l/nl, min(c*d, p/np));
    printf("%u\n", res / n);
}