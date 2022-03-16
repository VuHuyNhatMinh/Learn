#include <stdio.h>
#include <string.h>

void main()
{
    unsigned int a, b, c, d;
    scanf("%u%u%u%u", &a, &b, &c, &d);

    char s[100001];
    scanf("%s", s);
 
    unsigned int res = 0;
    for (unsigned int i = 0; i < strlen(s) ; i = i + 1)
    {
        if (s[i] == '1')
        {
            res = res + a;
        }

        if (s[i] == '2')
        {
            res = res + b;
        }

        if (s[i] == '3')
        {
            res = res + c;
        }

        if (s[i] == '4')
        {
            res = res + d;
        }
    }
 
    printf("%u\n", res);
}
