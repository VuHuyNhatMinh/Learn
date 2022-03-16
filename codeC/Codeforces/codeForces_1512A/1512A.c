#include <stdio.h>

void solve()
{
    // Input: Nhập số n và hai số ở số thứ tự 1, 2 để so sánh
    unsigned short n, a, b;
    scanf("%hu%hu%hu", &n, &a, &b);

    // Lỗi nhập số xảy ra là mình return ngay khi tìm được số spy, khiến cho các số phía sau bị nhập vào n, a, b
    char check = 1;
    for (int i = 3 ; i <= n ; i = i + 1)
    {
        unsigned short c;
        scanf("%hu", &c);
        if (check)
        {
            if (a == b)
            {
                if (c != a)
                {
                    printf("%d\n", i);
                    check = 0;
                }
            }
            else if (a != b)
            {
                if (c == a)
                {
                    printf("2\n");
                    check = 0;
                }
                else if (c == b)
                {
                    printf("1\n");
                    check = 0;
                }
            }
        }
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