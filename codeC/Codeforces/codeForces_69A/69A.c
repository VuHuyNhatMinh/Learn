#include <stdio.h>

int main(void)
{
    int n;
    scanf("%d", &n);

    int sumx, sumy, sumz;
    sumx = 0; sumy = 0; sumz = 0;
    for (int i = 0 ; i < n ; i = i + 1)
    {
        int x, y, z;
        scanf("%d%d%d", &x, &y, &z);
        sumx = sumx + x;
        sumy = sumy + y;
        sumz = sumz + z;
    }

    if ((sumx == 0) && (sumy == 0) && (sumz == 0))
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
    }
}