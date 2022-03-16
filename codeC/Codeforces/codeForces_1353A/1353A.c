#include <stdio.h>

void solve()
{
    unsigned int n, m;
    scanf("%u%u", &n, &m);
    if (n == 1)
    {
        printf("0\n");
    }
    else if (n == 2)
    {
        printf("%u\n", m);
    }
    else 
    {
        printf("%u\n", 2 * m );
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