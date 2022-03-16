#include <stdio.h>
#include <string.h>

int main(void)
{
    unsigned int n, m;
    scanf("%u%u", &n, &m);

    // Size of a, b
    char a[3001][11], b[3001][11];
    for (int i = 0 ; i < m ; i = i + 1)
    {
        scanf("%s%s", &a[i], &b[i]);
        if (strlen(a[i]) == strlen(b[i]))
        {
            i = i - 1;
            m = m - 1;
        }
    }

    for (unsigned int i = 0 ; i < n ; i = i + 1)
    {
        char temp[11];
        scanf("%s", temp);

        char ck = 0;
        for (unsigned int j = 0 ; j < m ; j = j + 1)
        {
            if (!strcmp(temp, a[j]))
            {
                if (strlen(a[j]) < strlen(b[j]))
                {
                    printf("%s ", a[j]);
                }
                else
                {

                    printf("%s ", b[j]);
                }

                ck = 1;
                break;
            }
        }

        if (!ck)
        {
            printf("%s ", temp);
        }
    }
}