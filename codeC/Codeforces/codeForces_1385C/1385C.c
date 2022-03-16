#include <stdio.h>

void solve()
{
    // Input
    unsigned int n;
    scanf("%u", &n);
    unsigned int a[n];
    for (int i = 0 ; i < n ; i = i + 1)
    {
        scanf("%u", &a[i]);
    }
    
    // Solve
    unsigned int pos = n - 1;
    while (pos > 0 && a[pos - 1] >= a[pos])
    {
        pos = pos - 1;
    }
    while (pos > 0 && a[pos - 1] <= a[pos])
    {
        pos = pos - 1;
    }
    printf("%u\n", pos);
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