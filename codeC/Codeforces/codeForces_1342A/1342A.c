#include <stdio.h>

void swap(unsigned long long int* x, unsigned long long int* y)
{
    unsigned long long int temp;
    temp = *x;
    *x = *y;
    *y = temp; 
}

void solve()
{
    unsigned long long int x, y;
    scanf("%llu%llu", &x, &y);
    if (x < y)
    {
        swap(&x, &y);
    }

    unsigned long long int a, b;
    scanf("%llu%llu", &a, &b);

    unsigned long long int sum = x + y;
    unsigned long long int res1 = a * sum;
    
    unsigned long long int minus= x - y;
    unsigned long long int res2 = b * y + a * minus;

    if (res1 > res2)
    {
        printf("%llu\n", res2);
    }
    else
    {
        printf("%llu\n", res1);
    }
}

int main(void)
{
    unsigned int t;
    scanf("%u",&t);
    while (t > 0)
    {
        solve();
        t = t - 1;
    }
}