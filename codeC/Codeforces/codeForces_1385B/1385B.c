#include <stdio.h>

void solve()
{
    unsigned short n;
    scanf("%hu", &n);
    
    char check[n + 1];
    for (int i = 0 ; i <= n ; i = i + 1)
    {
        check[i] = 0;
    }

    for (int i = 0 ; i < 2 * n ; i = i + 1)
    {
        unsigned short a;
        scanf("%hu", &a);
        if (check[a] == 0)
        {
            check[a] = 1;
        }
        else if (check[a] == 1)
        {
            printf("%hu ", a);
            check[a] = 2;
        }
    }

    printf("\n");
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