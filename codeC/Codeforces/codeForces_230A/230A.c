#include <stdio.h>
void swap(unsigned int *arr1, unsigned int *arr2, int c, int d)
{
    unsigned int temp;
    temp = arr1[c];
    arr1[c] = arr1[d];
    arr1[d] = temp;

    temp = arr2[c];
    arr2[c] = arr2[d];
    arr2[d] = temp;
}

void sort(unsigned int *a, unsigned int *b, unsigned int len)
{
    for (int i = 1 ; i < len ; i = i + 1)
    {
        for (int j = 0 ; j < i ; j = j + 1)
        {
            if (a[j] > a[i])
            {
                swap(a, b, i, j);
            }
            else if (a[i] == a[j])
            {
                if (b[j] > b[i])
                {
                    swap(a, b, i, j);
                }
            }
        }
    }
}

char solve(unsigned int s, unsigned int *x, unsigned int *y, unsigned int length)
{
    for (int i = 0 ; i < length ; i = i + 1)
    {
        if (s > x[i])
        {
            s = s + y[i];
        }
        else
        {
            return 0;
        }
    }
    return 1;
}

int main(void)
{
    unsigned int s, n;
    scanf("%u%u", &s, &n);
    
    unsigned int x[n], y[n];
    for (int i = 0 ; i < n ; i = i + 1)
    {
        scanf("%u%u", &x[i], &y[i]);
    }

    sort(x, y, n);
    char res = solve(s, x, y, n);
    if (res)
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
    }
}