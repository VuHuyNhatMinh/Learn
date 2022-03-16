#include <stdio.h>

void sort(unsigned int arr[], unsigned short n)
{
    for (int i = 1 ; i < n ; i = i + 1)
    {
        for (int j = 0 ; j < i ; j = j + 1)
        {
            if (arr[j] > arr[i])
            {
                unsigned int temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
            }
        }
    }
}

void solve()
{
    unsigned int a[3];
    scanf("%u%u%u", &a[0], &a[1], &a[2]);
    sort(a, 3);

    if (a[1] != a[2])
    {
        printf("NO\n");
    }
    else
    {
        printf("YES\n");
        for (int i = 0 ; i < 2 ; i = i + 1)
        {
            printf("%u ", a[i]);
        }
        printf("%u\n", a[0]);
    }
}

int main()
{
    unsigned short t;
    scanf("%hu", &t);
    while (t-- > 0)
    {
        solve();
    }
    return 0;
}