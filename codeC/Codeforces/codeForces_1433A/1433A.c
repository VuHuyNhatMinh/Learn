#include <stdio.h>

void solve()
{
    unsigned short x;
    scanf("%hu", &x);
    
    unsigned short k = x % 10;
    unsigned short cnt = 0;
    while (x > 0)
    {
        cnt = cnt + 1;
        x = x / 10;
    }

    unsigned short res = 0;
    for(int i = 1 ; i <= 4 ; i = i + 1)
    {
        if (i <= cnt)
        {
            res = res + k * i;
        }
        else
        {
            res = res + (k - 1) * i;
        }
    }
    printf("%hu\n", res);
}

int main()
{
    unsigned short t;
    scanf("%hu", &t);
    while(t-- > 0)
    {
        solve();
    }
    return 0;
}