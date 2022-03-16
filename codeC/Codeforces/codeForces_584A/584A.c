#include <stdio.h>

int main(void)
{
    unsigned int n, t;
    scanf("%u%u", &n, &t);
    if (n == 1 && t == 10)
    {
        printf("-1\n");
    }
    else if (n >= 2 && t == 10)
    {
        for(int i = 1; i < n ; i = i + 1)
        {
            printf("1");
        }
        printf("0\n");
    }
    else 
    {
        for(int i = 0 ; i < n ; i = i + 1)
        {
            printf("%u", t);
        }
    }
}