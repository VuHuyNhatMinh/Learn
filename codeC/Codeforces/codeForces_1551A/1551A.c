#include <stdio.h>
void solve()
{
    unsigned int n;
    scanf("%u", &n);

    unsigned int c1, c2;

    char temp = n % 3;
    if (temp % 2)
    {
        c2 = (n - temp) / 3;
        c1 = n - 2 * c2;
    }
    else
    {
        c1 = (n - temp) / 3;
        c2 = (n - c1) / 2;
    }

    printf("%u %u\n", c1, c2);
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

