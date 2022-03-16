#include <stdio.h>
#include <string.h>

int main(void)
{
    unsigned int n;
    scanf("%u", &n);

    unsigned int cnt1, cnt2;
    cnt2 = 0;

    char a[11], b[11];
    scanf("%s", a);
    cnt1 = 1;

    for (int i = 1 ; i < n ; i = i + 1)
    {
        char s[11];
        scanf("%s", s);
        if (strcmp(s, a))
        {
            strcpy(b, s);
            cnt2 = cnt2 + 1;
        }
        else
        {
            cnt1 = cnt1 + 1;
        }
    }

    if (cnt1 > cnt2)
    {
        printf("%s\n", a);
    }
    else
    {
        printf("%s\n", b);
    }
}