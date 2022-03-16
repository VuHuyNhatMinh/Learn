#include <stdio.h>

void solve()
{
    unsigned int n;
    scanf("%u", &n);

    for (int i = 0 ; i < n - 1 ; i = i + 1)
    {
        printf("%d ", i + 2);
    }
    printf("1\n");
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