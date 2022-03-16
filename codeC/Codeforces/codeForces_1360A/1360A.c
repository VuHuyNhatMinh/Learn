#include <stdio.h>
unsigned short area(unsigned short wid, unsigned short len)
{
    if (2 * wid >= len)
    {
        printf("%hu\n", 4 * wid * wid);
    }
    else
    {
        printf("%hu\n", len * len);
    }
}
int main()
{
    unsigned short t;
    scanf("%hu", &t);
    while (t > 0)
    {
        unsigned short a, b;
        scanf("%hu%hu", &a, &b);
        if (a < b)
        {
            area(a, b);
        }
        else
        {
            area(b, a);
        }
        t = t - 1;
    }
    return 0;
}