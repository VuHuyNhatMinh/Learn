#include <stdio.h>

int main()
{
    unsigned short t;
    scanf("%hu", &t);

    while (t > 0)
    {
        unsigned int n;
        scanf("%u", &n);
        if (n % 4)
        {
            printf("NO\n");
        }
        else
        {
            printf("YES\n");
            for (int i = 2 ; i <= n ; i = i + 2)
            { 
                printf("%d ", i);
            }

            for (int i = 1 ; i <= n - 3 ; i = i + 2)
            {
                printf("%d ", i);
            }

            printf("%u\n", (3 * n - 2) / 2);
        }
        t = t - 1;
    }
    return 0;
}