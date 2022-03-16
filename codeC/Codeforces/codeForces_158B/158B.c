#include <stdio.h>

int main(void)
{
    unsigned long int n;
    scanf("%lu", &n);

    unsigned long int num1, num2, num3;
    num1 = num2 = num3 = 0;

    unsigned long int res = 0;
    for(unsigned long int i = 0; i < n ; i = i + 1)
    {
        int temp;
        scanf("%d", &temp);
        if (temp == 1)
        {
            num1 = num1 + 1;
        }
        else if (temp == 2)
        {
            num2 = num2 + 1;
        }
        else if (temp == 3)
        {
            num3 = num3 + 1;
        }
        else if (temp == 4)
        {
            res = res + 1;
        }
    }

    res = res + num3;
    if (num3 <= num1)
    {
        num1 = num1 - num3;
    }
    else
    {
        num1 = 0;
    }

    unsigned long int temp = num1 + 2*num2;
    //printf("%lu %lu %lu\n", num1, num2, temp);
    if (temp % 4)
    {
        res = res + temp / 4 + 1;
    }
    else
    {
        res = res + temp / 4;
    }

    printf("%lu\n", res);
}