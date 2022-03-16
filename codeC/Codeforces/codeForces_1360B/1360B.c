#include <stdio.h>

void solve()
{
    unsigned short n;
    scanf("%hu", &n);
 
    unsigned short s[n];
    for (int i = 0 ; i < n ; i = i + 1)
    {
        scanf("%hu", &s[i]);
    }
 
    for (int i = 1 ; i < n ; i = i + 1)
    {
        for (int j = 0 ; j < i ; j = j + 1)
        {
            if (s[j] > s[i])
            {
                unsigned short temp;
                temp = s[i];
                s[i] = s[j];
                s[j] = temp;
            }
        }
    }
 
    unsigned short res = 1001;
    for (int i = 1 ; i < n ; i = i + 1)
    {
        if (s[i] - s[i - 1] < res)
        {
            res = s[i] - s[i - 1];
        }
    }
 
    printf("%hu\n", res);
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