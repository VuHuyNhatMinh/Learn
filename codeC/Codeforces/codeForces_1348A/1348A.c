#include <stdio.h>

void solve()
{
    unsigned short n;
    scanf("%hu", &n);

    unsigned int sum_1 = 1 << n;
    for (int i = 1 ; i < n / 2 ; i = i + 1)
    {
        sum_1 = sum_1 + (1 << i);
    }

    unsigned int sum_2 = 0;
    for (int i = n / 2 ; i < n ; i = i + 1)
    {
        sum_2 = sum_2 + (1 << i);
    }

    printf("%u\n", sum_1 - sum_2);
}


int main()
{
    unsigned short t;
    scanf("%hu", &t);
    while (t-- > 0)
    {
        solve();
    }
    return 0;
}