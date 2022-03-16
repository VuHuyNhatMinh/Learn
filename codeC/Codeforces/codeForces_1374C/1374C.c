#include <stdio.h>

void check(int* a, unsigned int len)
{
    for (int i = 0 ; i < len ; i = i + 1)
    {
        printf("%d ", a[i]);
    }
    printf("\n");
}

void push(int i, int* a, unsigned int* len)
{
    a[*len] = i;
    *len = *len + 1;
}

void pop(int *a, unsigned int* len)
{
    a[*len] = 0;
    *len = *len - 1;
}

void solve()
{
    unsigned int n;
    scanf("%u", &n);

    char s[n + 1];
    scanf("%s", s);

    char ck = 0;
    int a[n + 1];
    unsigned int cnt = 0;
    for (int i = 0 ; i < n ; i = i + 1)
    {
        if (s[i] == '(')
        {
            push(i, a, &cnt);
        }
        else if (s[i] == ')')
        {
            if (cnt > 0)
            {
                pop(a, &cnt);
            }
        }
    }

    // check(a, cnt);

    unsigned int res = 0;
    res = res + cnt;
    printf("%u\n", res);
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