#include <stdio.h>
#include <math.h>

void merge(unsigned int* arr, int start, int mid, int end)
{
    unsigned int temp[end - start + 1];

    int i = start;
    int j = mid + 1;
    int k = 0;

    while (i <= mid && j <= end)
    {
        if (arr[i] < arr[j])
        {
            temp[k] = arr[i];
            k = k + 1;
            i = i + 1;
        }
        else 
        {
            temp[k] = arr[j];
            k = k + 1;
            j = j + 1;
        }
    }

    while (i <= mid)
    {
        temp[k] = arr[i];
        k = k + 1;
        i = i + 1;
    }

    while (j <= end)
    {
        temp[k] = arr[j];
        k = k + 1;
        j = j + 1;
    }

    for (i = start; i <= end ; i = i + 1)
    {
        arr[i] = temp[i - start];
    }
}

void mergeSort(unsigned int* arr, int start, int end)
{
    if (start < end)
    {
        int mid = (start + end) / 2;
        mergeSort(arr, start, mid);
        mergeSort(arr, mid + 1, end);
        merge(arr, start, mid, end);
    }
}

unsigned int findMin(unsigned int a, unsigned int b)
{
	if (a < b)
	{
		return a;
	}
	else
	{
		return b;
	}
}

void solve(unsigned int n, unsigned int m, unsigned int* a, unsigned int* b)
{
    char ck[m + 1];
    for (unsigned int i = 0 ; i < m ; i = i + 1)
    {
        ck[i] = 1;
    }

    unsigned int res = 0;
    for (unsigned int i = 0 ; i < n ; i = i + 1)
    {
        for (unsigned int j = 0 ; j < m ; j = j + 1)
        {       
            if (ck[j] == 1)
            {
                if (abs(a[i] - b[j]) <= 1)
                {
                    res = res + 1;
                    ck[j] = 0;
                    break;
                }
            }
        }
}
    
    printf("%u \n", res);
}

int main(void)
{
    /* Input */
    unsigned int n;
    scanf("%u", &n);

    unsigned int a[n + 1];
    for (unsigned int i = 0 ; i < n ; i = i + 1)
    {
        scanf("%u", &a[i]);
    }

    unsigned int m;
    scanf("%u", &m);

    unsigned int b[m + 1];
    for (unsigned int i = 0 ; i < m ; i = i + 1)
    {
        scanf("%u", &b[i]);
    }

    /* Sort */
    mergeSort(a, 0, n - 1);
    mergeSort(b, 0, m - 1);

    /* Solve */
    if (n < m)
    {
        solve(n, m, a, b);
    }
    else
    {
        solve(m, n, b, a);
    }
}