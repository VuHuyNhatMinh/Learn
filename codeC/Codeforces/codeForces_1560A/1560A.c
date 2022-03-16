#include <stdio.h>

void solve()
{
    unsigned int k;
    scanf("%u", &k);

    unsigned int cnt = 0;
    for (int i = 0 ; i < k ; i = i + 1)
    {
        cnt = cnt + 1;
        while ((cnt % 3 == 0) || (cnt % 10 == 3))
        {
            cnt = cnt + 1;
        }
    }
    printf("%u\n", cnt);    
}

int main(void)
{
    unsigned int t;
    scanf("%u", &t);
    for (int i = 0 ; i < t ; i = i + 1)
    {
        solve();
    }    
}