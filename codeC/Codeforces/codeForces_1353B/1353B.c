#include <stdio.h>

unsigned short getAndSort(unsigned short arr[], unsigned short size)
{
    for (int i = 0 ; i < size ; i = i + 1)
    {
        scanf("%hu", &arr[i]);
    }

    for (int i = 1 ; i < size ; i = i + 1)
    {
        for (int j = 0 ; j < i ; j = j + 1)
        {
            if (arr[j] > arr[i])
            {
                unsigned short temp;
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

int main()
{
    unsigned short t;
    scanf("%hu", &t);
    while (t > 0)
    {
        unsigned short n, k;
        scanf("%hu%hu", &n, &k);

        unsigned short a[n], b[n];
        getAndSort(a, n);
        getAndSort(b, n);

        unsigned short res = 0;
        for (int i = 0 ; i < n ; i = i + 1)
        {
            if (i < k)
            {
                if (a[i] < b[n - i - 1])
                {
                    res = res + b[n - i - 1];
                    continue;
                }            
            }
            res = res + a[i];
        }

        printf("%hu\n", res);
        t = t - 1;
    }
    return 0;
}