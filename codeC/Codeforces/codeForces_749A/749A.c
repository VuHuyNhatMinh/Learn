#include <stdio.h>

int main()
{
    unsigned int n;
    scanf("%u", &n);
    unsigned int k = n / 2;
    
    printf("%u\n", k);
    unsigned short r = n % 2;
    if (r)
    {
        for (int i = 0 ; i < k - 1 ; i = i + 1)
        {
            printf("2 ");
        }
        printf("3\n");
    }
    else
    {
        for (int i = 0 ; i < k ; i = i + 1)
        {
            printf("2 ");
        }
        printf("\n");
    }
    return 0;
}