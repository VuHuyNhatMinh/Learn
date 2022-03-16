#include <stdio.h>

void solve()
{
    unsigned int a, b;
    scanf("%u %u", &a, &b);

    if (a == b)
    {
        printf("0\n");
    }
    else if (a < b)
    {
        unsigned int temp = b - a;
        if (temp % 2 == 1)
        {
            printf("1\n");
        }
        else
        {
            printf("2\n");
        }
    }
    else if (a > b)
    {
        unsigned int temp = a - b;
        if (temp % 2 == 0)
        {
            printf("1\n");
        }
        else
        {
            printf("2\n");
        }
        
    }
}

int main(void)
{
    unsigned int t;
    scanf("%u", &t);
    while (t > 0)
    {
        t = t - 1;
        solve();
    }
}