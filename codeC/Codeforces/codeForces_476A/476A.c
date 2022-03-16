#include <stdio.h>

int main(void)
{
    unsigned int n, m;
    scanf("%u%u", &n, &m);
    
    unsigned int cnt1, cnt2;
    cnt1 = n % 2;
    cnt2 = n / 2;

    while (1)
    {
        unsigned int sum = cnt1 + cnt2;
        if (sum % m == 0)
        {
            printf("%u\n", sum);
            break;
        }
        else
        {
            if (cnt2 == 0)
            {
                printf("-1\n");
                break;
            }
            else if (cnt2 > 0)
            {            
                cnt2 = cnt2 - 1;
                cnt1 = cnt1 + 2;
            }
        }
    }
}