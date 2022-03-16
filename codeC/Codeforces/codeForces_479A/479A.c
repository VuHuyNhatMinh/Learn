#include <stdio.h>
int max(int x, int y)
{
    if (x  < y)
    {
        return y;
    }
    else
    {
        return x;
    }
}

int main(void)
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    int sum0, sum1, sum2, sum3, sum4, sum5;
    sum0 = a+b+c;
    sum1 = a*b+c;
    sum2 = a+b*c;
    sum3 = (a+b)*c;
    sum4 = a*(b+c);
    sum5 = a*b*c;

    int res = max(sum0, max(sum1, max(sum2, max(sum3, max(sum4, sum5)))));
    printf("%d\n", res);
}