#include <stdio.h>
#include <math.h>

int main(void)
{
    unsigned int n, x;
    scanf("%u%u", &n, &x);

    unsigned int res = 0;
    for(unsigned int i = 1 ; i <= sqrt(x) ; i = i + 1)
    {
        if (x % i == 0)
        {
            unsigned int temp = x / i;
            if (i == temp && i <= n)
            {
                res = res + 1;
            }
            else if ((i <= n) && (temp <= n))
            {
                res = res + 2;
            }
        }
    }

    printf("%u\n", res);
}