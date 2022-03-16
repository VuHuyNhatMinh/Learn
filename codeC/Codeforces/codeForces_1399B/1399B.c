#include <stdio.h>

int main()
{
    unsigned short t;
    scanf("%hu", &t);
    while (t > 0)
    {
        unsigned short n;
        scanf("%hu", &n);

        unsigned int a[n], b[n];
        unsigned int min_a, min_b;
        min_a = min_b = 1000000001;
        for (int i = 0 ; i < n ; i = i + 1)
        {
            scanf("%u", &a[i]);
            if (a[i] < min_a)
            {
                min_a = a[i];
            }
        }

        for (int i = 0 ; i < n ; i = i + 1)
        {
            scanf("%u", &b[i]);
            if (b[i] < min_b)
            {
                min_b = b[i];
            }
        }

        unsigned long long res = 0;
        for (int i = 0 ; i < n ; i = i + 1)
        {
            if (a[i] - min_a < b[i] - min_b)
            {
                res = res + b[i] - min_b;
            }
            else 
            {
                res = res + a[i] - min_a;
            }
        }

        printf("%llu\n", res);
        t = t - 1;
    }
    return 0;
}