#include <stdio.h>
#include <string.h>

int solve()
{
    unsigned short check[26];
    for(int i = 1 ; i <= 26 ; i = i + 1)
    {
        check[i] = 1;
    }

    unsigned short n;
    scanf("%hu", &n);
    getchar();

    char str[n];
    fgets(str, n + 1, stdin);
    getchar();

    char key = str[0];
    check[(int)str[0] - 64] = 0;

    for (int i = 1 ; i < strlen(str); i = i + 1)
    {
        if ((check[(int)str[i] - 64] == 1) || (key == str[i]))
        {
            check[(int)str[i] - 64] = 0;
            key = str[i];
        }
        else
        {
            return 0;
        } 
    }
    return 1;
}

int main()
{
    unsigned short t;
    scanf("%hu", &t);
    while (t-- > 0)
    {
        int check = solve();
        if (check)
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }
    }
    return 0;
}