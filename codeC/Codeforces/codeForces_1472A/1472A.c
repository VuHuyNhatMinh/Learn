#include <stdio.h>

void solve()
{
    unsigned int w, h, n;
    scanf("%u %u %u", &w, &h, &n);
    
    unsigned int sum = 1;
    while (1)
    {
        if (w % 2 == 0)
        {
            sum = sum * 2;
            w = w / 2;
        }
        else if (h % 2 == 0)
        {
            sum = sum * 2;
            h = h / 2;
        }
        else
        {
            break;
        }
    }

    if (sum >= n)
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
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