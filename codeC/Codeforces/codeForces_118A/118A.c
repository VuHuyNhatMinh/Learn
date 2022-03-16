#include <stdio.h>
#include <string.h>

int main(void)
{
    char vow[12] = {'A', 'O', 'Y', 'E', 'U', 'I', 'a', 'o', 'y', 'e', 'u', 'i'};
    char str[101];
    fflush(stdin);
    scanf("%s", str);
    for(char i = 0; i < strlen(str); i = i + 1)
    {
        for(char j = 0; j < 12 ; j = j + 1)
        {
            if (str[i] == vow[j])
            {
                str[i] = ' ';
            }
        }

        if (str[i] != ' ')
        {
            if (str[i] >= 'A' && str[i] <= 'Z')
            {
                str[i] = str[i] + 32;
            }

            printf(".%c", str[i]);
        }
    }
    printf("\n");
}