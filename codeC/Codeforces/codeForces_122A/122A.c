#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);

    int lk[14] = {4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777};
    for (int i = 0 ; i < 14 && lk[i] <= n; i = i + 1)
    {
        if (!(n % lk[i]))
        {
            printf("YES\n");
            return 0;
        }
    }
    printf("NO\n");
    return 0;
}