#include <stdio.h>
void solve()
{
    unsigned short n;
    scanf("%hu", &n);
    
    unsigned short rem_0, rem_1;
    rem_0 = rem_1 = 0;
    for(int i = 0 ; i < n ; i = i + 1)
    {
        unsigned short a;
        scanf("%hu", &a);
        if (a % 2 != i % 2)
        {
            if (i % 2)
            {
                rem_1 = rem_1 + 1;
            }
            else
            {
                rem_0 = rem_0 + 1;
            }
        }
    }

    if (rem_0 != rem_1)
    {
        printf("-1\n");
    }
    else 
    {
        printf("%hu\n", rem_0);
    }
}

int main()
{
    unsigned short t;
    scanf("%hu", &t);
    while (t > 0)
    {
        solve();
        t = t - 1;
    }
    return 0;
}