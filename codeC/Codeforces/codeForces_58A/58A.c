#include <stdio.h>
#include <string.h>
 
int main()
{
    char s[101];
    scanf("%s", s);
 
    int cnt = 0;
    char ck;
    char string[6] = "hello";
    for (int i = 0 ; i < 5 ; i = i + 1)
    {
        /* Find the position of the character needed in the input string. */
        for (; cnt  < strlen(s) ; cnt = cnt + 1)
        {
            if (s[cnt] == string[i])
            {
                break;
            }
        }
 
        /* Check if the position is less than length of the input string.*/
        if (cnt < strlen(s))
        {
            cnt = cnt + 1;
        }
        else
        {
            printf("NO\n");
            return 0;
        }
    }
    printf("YES\n");
    return 0;
}
