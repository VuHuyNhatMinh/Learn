#include <stdio.h>

int main()
{
    unsigned short n, k;
    scanf("%hu%hu", &n, &k);
    unsigned short y[n];
    for (int i = 0 ; i < n ; i = i + 1)
    {
        scanf("%hu", &y[i]);
    }

    for (int i = 1 ; i < n ; i = i + 1)
    {
        for (int j = 0 ; j < i ; j = j + 1)
        {
            if (y[i] < y[j])
            {
                unsigned short temp;
                temp = y[i];
                y[i] = y[j];
                y[j] = temp;
            }
        }
    }

    unsigned short res = 0;
    for (int i = 2 ; i < n ; i = i + 3)
    {
        if (y[i] + k <= 5)
        {
            res = res + 1;
        }
        else
        {
            break;
        }
    }
    printf("%hu\n", res);
    return 0;
}