#include <stdio.h>

void solve()
{
    unsigned int n;
    scanf("%u", &n);
    printf("%u\n", n / 2);
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