#include <stdio.h>

unsigned int findMax(unsigned int a, unsigned int b)
{
	if (a > b)
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
    unsigned int n;
    scanf("%u", &n);

    // Calculate the number of 0 in i-th position. Starting from 1 to n.
    unsigned int sum[n + 2];
    sum[0] = 0;
    for (unsigned int i = 1 ; i <= n ; i = i + 1)
    {
        int temp;
        scanf("%d", &temp);
        if (temp == 0)
        {
            sum[i] = sum[i - 1] + 1;
        }
        else
        {
            sum[i] = sum[i - 1];
        }
    }


    unsigned int res = 0;
    for (unsigned int i = 0 ; i < n ; i = i + 1)
    {
        // Numbers of 1 at position i
        unsigned int num = i - sum[i];

        for (unsigned int j = i + 1 ; j <= n ; j = j + 1)
        {
           // Numbers of 0 between i + 1 and j
            unsigned int len0 = sum[j] - sum[i];

            // Numbers of 1 between j + 1 and n;
            unsigned int len1 = (n - j) - (sum[n] - sum[j]);

            // Result
            res = findMax(res, num + len0 + len1);
        }
    }

    printf("%u\n", res);
}
