#include <stdio.h>
#define max 2000000
int main(void)
{
    unsigned int n;
    scanf("%u", &n);
    
    char ck[max + 1];
    for(unsigned int i = 0; i < max ; i = i + 1)
    {
        ck[i] = 1;
    }

    for(unsigned int i = 2; i < max ; i = i + 1)
    {
        if (ck[i] == 1)
        {
            printf("%u ", i);
            n = n - 1;
            for(unsigned int j = 2; j < max/i ; j = j + 1)
            {
                ck[i * j] = 0;
            }
        }

        if (n == 0)
        {
            break;
        }
    }

    printf("\n");
}