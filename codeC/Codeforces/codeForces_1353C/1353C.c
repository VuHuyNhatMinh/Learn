#include <stdio.h>

void solve()
{
    unsigned long long int n;
    scanf("%llu", &n);

    unsigned long long int res = (n - 1) * n * (n + 1) / 3; 
    printf("%llu\n", res);
}

int main(void)
{
    unsigned int t;
    scanf("%u", &t);
    while (t > 0)
    {
        solve();
        t = t - 1;
    }
}