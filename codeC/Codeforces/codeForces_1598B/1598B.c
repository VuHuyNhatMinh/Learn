#include <stdio.h>

void result(char ck)
{
    if (ck)
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
    }
}

void solve()
{
    // Input
    unsigned int n;
    scanf("%u", &n);

    unsigned int a[1001][5];
    for (int i = 0 ; i < n ; i = i + 1)
    {
        for (int j = 0 ; j < 5 ; j = j + 1)
        {
            scanf("%u", &a[i][j]);
        }
    }

    // Solve
    char res = 0;
    // Chose 2 different days    
    for (int i = 0 ; i < 5 ; i = i + 1)
    {
        for (int j = i + 1 ; j < 5 ; j = j + 1)
        {
            unsigned int cnt1, cnt2, cnt0;
            cnt0 = cnt1 = cnt2 = 0;

            for (int k = 0 ; k < n ; k = k + 1)
            {
                if (a[k][i] == 1)
                {
                    cnt1 = cnt1 + 1;
                }
                
                if (a[k][j] == 1)
                {
                    cnt2 = cnt2 + 1;
                }
                
                if (a[k][i] == 0 && a[k][j] == 0)
                {
                    cnt0 = cnt0 + 1;
                } 
            }

            if (cnt1 >= n / 2 && cnt2 >= n / 2 && cnt0 == 0)
            {
                res = 1;
            }
        }
    }

    // Print result
    result(res);
}

int main(void)
{
    unsigned int t;
    scanf("%u", &t);
    while (t > 0)
    {
        solve();
        t = t - 1;
    }
}