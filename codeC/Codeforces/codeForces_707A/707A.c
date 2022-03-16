#include <stdio.h>

int main()
{
    unsigned int n, m;
    scanf("%u %u", &n, &m);

    getchar();
    for (int i = 0 ; i < n ;i = i + 1)
    {
        for(int j = 0 ; j < m ; j = j + 1)
        {
            char ch;
            scanf("%c", &ch);
            getchar();

            if (ch == 'C' || ch == 'M' || ch == 'Y')
            {
                printf("#Color\n");
                return 0;
            }
        }
    }

    printf("#Black&White\n");
    return 0;
}