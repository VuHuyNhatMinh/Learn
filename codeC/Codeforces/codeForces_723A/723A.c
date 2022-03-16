#include <stdio.h>

int main()
{
    unsigned short x[3];
    for (int i = 0 ; i < 3 ; i = i + 1)
    {
        scanf("%hu", &x[i]);
    }

    for (int i = 1 ; i < 3 ; i = i + 1)
    {
        for (int j = 0 ; j < i ; j = j + 1)
        {
            if (x[i] < x[j])
            {
                unsigned temp;
                temp = x[i];
                x[i] = x[j];
                x[j] = temp;
            }
        }
    }

    for (int i = 0 ; i < 3 ; i = i + 1)
    {
        printf("%hu ", x[i]);
    }

    /*
    unsigned short temp;
    temp = (x[0] + x[2]) / 2;
    printf("%hu\n", temp);
    if (temp > x[1])
    {
        printf("%hu\n", (x[2] - temp) + (temp - x[0]) + (temp - x[1]));
    }
    else
    {
        printf("%hu\n", (x[2] - temp) + (temp - x[0]) + (x[1] - temp));
    }
    */

    printf("%hu\n", x[2] - x[1] + x[1] - x[0]);
    return 0;


}
