#include <stdio.h>

void solve()
{
    unsigned short n;
    scanf("%hu", &n);
    getchar();
    
    unsigned short checkCol[n], checkRow[n];
    for (int i = 0 ; i < n ; i = i + 1)
    {
        checkCol[i] = 0;
        for (int j = 0 ; j < n ; j = j + 1)
        {
            checkRow[j] = 0;
        }
    }

    unsigned short cntRow, cntCol;
    cntRow = cntCol = 0;
    for (int i = 0 ; i < n ; i = i + 1)
    {
        for (int j = 0; j < n ; j = j + 1)
        {
            char c = getchar();
            if (c == '*')
            {
                if (checkCol[i] == 0)
                {
                    checkCol[i] = 1;
                    cntCol = cntCol + 1;
                }
                if (checkRow[j] == 0)
                {
                    checkRow[j] = 1;
                    cntRow = cntRow + 1;    
                }
            }
        }
        getchar();
    }

    if (cntCol == 1)
    {
        for (int i = 0; i < n ; i = i + 1)
        {
            if (checkCol[i] == 0)
            {
                checkCol[i] = 1;
                cntCol += 1;
                break;
            }
        }
    }

    if (cntRow == 1)
    {
        for (int i = 0; i < n ; i = i + 1)
        {
            if (checkRow[i] == 0)
            {
                checkRow[i] = 1;
                cntRow += 1;
                break;
            }
        }
    }
    /*
    printf("Col %hu ", cntCol);
    for (int i = 0 ; i < n ; i = i + 1)
    {
        printf("%hu ", checkCol[i]);
    }
    printf("\n");

    printf("Row %hu ", cntRow);
    for (int i = 0 ; i < n ; i = i + 1)
    {
        printf("%hu ", checkRow[i]);
    }
    printf("\n");
    */

    for (int i = 0; i < n ; i = i + 1)
    {
        for (int j = 0 ; j < n ;j = j + 1)
        {
            if (checkCol[i] && checkRow[j])
            {
                printf("*");
            }
            else 
            {
                printf(".");
            }
        }
        printf("\n");
    }
}

int main()
{
    unsigned short t;
    scanf("%hu", &t);
    while (t > 0)
    {
        solve();
        t = t - 1;
    }
    return 0;
}