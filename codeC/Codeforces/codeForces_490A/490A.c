#include <stdio.h>

int main()
{
    unsigned short n;
    scanf("%hu", &n);

    unsigned short dir[4][n], len[4];
    len[1] = len[2] = len[3] = 0;
    for (int i = 0 ; i < n ; i = i + 1)
    {
        unsigned short a;
        scanf("%hu", &a);
        dir[a][len[a]] = i + 1;
        len[a] = len[a] + 1;
    }

    unsigned short res;
    if (len[1] <= len[2] && len[1] <= len[3])
    {
        res = len[1];
    }
    else if (len[2] <= len[1] && len[2] <= len[3])
    {
        res = len[2];
    }
    else if (len[3] <= len[1] && len[3] <= len[2])
    {
        res = len[3];
    }

    printf("%hu\n", res);
    for (int i = 0 ; i < res ; i = i + 1)
    {
        printf("%hu %hu %hu\n", dir[1][i], dir[2][i], dir[3][i]);
    }
    return 0;
}