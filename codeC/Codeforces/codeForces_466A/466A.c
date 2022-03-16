#include <stdio.h>

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

int main(void)
{
    unsigned int n, m, a, b;
    scanf("%u%u%u%u", &n, &m, &a, &b);

    unsigned int res = a * n;
    for (unsigned int i = 0 ; i <= n / m ; i = i + 1)
    {
        if (i * (b - m * a) + n * a > 0)
        {
            res = findMin(res, i * (b - m * a) + n * a);
        }
    }

    if (n % m)
    {
        res = findMin(res, b * (n / m + 1));
    }
    
    printf("%u\n", res);
}