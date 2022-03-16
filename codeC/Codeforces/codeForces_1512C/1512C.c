#include <stdio.h>
#include <string.h>

void solve()
{
    // Input a: 0, b: 1
    int a, b;
    scanf("%d%d", &a, &b);

    // Input: string
    char s[a + b + 1];
    scanf("%s", s);
    unsigned long int n = strlen(s);


    // Solve
    for (int i = 0 ; i < n / 2 ; i = i + 1)
    {
        if (s[i] != '?')
        {
            if (s[n - i - 1] == '?')
            {
                s[n - i - 1] = s[i];
            }
            else if (s[i] != s[n - i - 1])
            {
                printf("-1\n");
                return;
            }

        }
        else if (s[i] == '?')
        {
            if (s[n - i - 1] != '?')
            {
                s[i] = s[n - i - 1];
            }
        }

        if (s[i] == '0')
        {
            a = a - 2;
        }
        else if (s[i] == '1')
        {
            b = b - 2;
        }
    }
    // printf("%d %d\n", a, b);
    // puts(s);

    if ((a >= 0) && (b >= 0))
    {        
        if (a % 2 && b % 2)
        {
            printf("-1\n");
            return;
        }
        else if (a % 2 && b % 2 == 0)
        {
            if (s[n / 2] == '1')
            {
                printf("-1\n");
                return;
            }
            s[n / 2] = '0';
            a = a - 1;    
        }
        else if (a % 2 == 0 && b % 2)
        {
            if (s[n / 2] == '0')
            {
                printf("-1\n");
                return;
            }
            s[n / 2] = '1';
            b = b - 1;
        }
    }
    else
    {
        printf("-1\n");
        return;
    }
    // printf("%d %d\n", a, b);
    // puts(s);

    for (int i = 0 ; i < n / 2; i = i + 1)
    {
        // printf("%d %d\n", a, b);
        // puts(s);
        if (s[i] == '?')
        {
            if (a > 1)
            {
                s[i] = s[n - i - 1] = '0';
                a = a - 2;
            }
            else if (b > 1)
            {
                s[i] = s[n - i - 1] = '1';
                b = b - 2;
            }
            else
            {
                printf("-1\n");
                return;
            }
        }
    }
    puts(s);
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