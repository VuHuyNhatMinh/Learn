#include <stdio.h>

int main(void)
{
    unsigned int n;
    scanf("%u", &n);

    unsigned int a[n + 1];
    for (int i = 0 ; i < n ; i = i + 1)
    {
        scanf("%u", &a[i]);
    }

    unsigned int sum[2];
    sum[0] = sum[1] = 0;
    char pos = 0;

    unsigned int l, r;
    l = 0;
    r = n - 1;
    while (n > 0)
    {
        if (a[l] > a[r])
        {
            sum[pos] = sum[pos] + a[l];
            l = l + 1;
            n = n - 1;
        }
        else
        {
            sum[pos] = sum[pos] + a[r];
            r = r - 1;
            n = n - 1;
        }
        pos = 1 - pos;
    }
    printf("%u %u\n", sum[0], sum[1]);
}