#include <stdio.h>
#include <string.h>

int main(void)
{
    char s[101];
    scanf("%s", s);

    char check = 1;
    for (int i = strlen(s) - 1 ; i >= 0 ; i = i - 1)
    {
        if (i)
        {
            if ((s[i] >= 'A') && (s[i] <= 'Z'))
            {
                continue;
            }
            check = 0;
        }
    }

    if (check)
    {
        for(int i = 0; i < strlen(s); i = i + 1)
        {
            if ((s[i] >= 'A') && (s[i] <= 'Z'))
            {
                s[i] = s[i] + 32;
            }
            else if ((s[i] >= 'a') && (s[i] <= 'z'))
            {
                s[i] = s[i] - 32;
            }
        }
    }

    puts(s);
}