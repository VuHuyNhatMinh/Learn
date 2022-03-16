#include <stdio.h>

int main()
{
    unsigned short t;
    scanf("%hu", &t);
    while (t > 0)
    {
        unsigned int x, y, n;
        scanf("%u%u%u", &x, &y, &n);

        char check = 1;
        for (int i = n ; i > 0 ; i = i - 1)
        {
            if (i % x >= y)
            {
                i = i - i % x + y;
                check = 0;
                printf("%d\n", i);
                break;
            }
            else
            {
                i = i - i % x;
            }
        }

        if (check)
        {
            printf("0\n");
        }
        t = t - 1;
    }
    return 0;
}