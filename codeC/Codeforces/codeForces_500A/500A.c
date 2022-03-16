#include <stdio.h>

int main(void)
{
    unsigned int n, t;
    scanf("%u %u", &n, &t);

    unsigned int pos = 1;
    for (unsigned int i = 1 ; i < n ; i = i +1)
    {
        unsigned int a;
        scanf("%u", &a);

        if (pos == i)
        {    
            pos = pos + a;
        }

        printf("%u %u\n", pos, t);
        
        if (pos > t)
        {
            printf("NO\n");
            return 1;
        }
        else if (pos == t)
        {
            printf("YES\n");
            return 1;
        }        
    }
}