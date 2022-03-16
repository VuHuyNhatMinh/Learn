#include <stdio.h>
 
int solve()
{
    unsigned int n;
    scanf("%u", &n);
    
    unsigned int cnt_1, cnt_2;
    cnt_1 = cnt_2 = 0;
 
    for (int i = 0 ; i < n ; i = i + 1)
    {
        unsigned int temp;
        scanf("%u", &temp);
        if (temp == 1)
        {
            cnt_1 = cnt_1 + 1;
        }
        else if (temp == 2)
        {
            cnt_2 = cnt_2 + 1;
        }
    }

    if ((cnt_1 + 2*cnt_2) % 2 == 0)
    {
        unsigned int sum = (cnt_1 + 2*cnt_2) / 2;
        if ((sum % 2 == 0) || (sum % 2 == 1 && cnt_1 != 0))
        {
            printf("YES\n");
            return 0;
        }
    }
    printf("NO\n");
    return 0;
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