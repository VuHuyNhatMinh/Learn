#include <iostream>
using namespace std;

void solve()
{
    unsigned short n;
    cin >> n;
    string s;
    cin >> s;
    for (char c = 'A' ; c <= 'Z' ; c = c + 1)
    {
        unsigned short first = n;
        unsigned short last = 0;

        // Tìm kiếm sự xuất hiện đầu tiên và cuối cùng của kí tự s[i]
        for (int i = 0 ; i < n ; i = i + 1)
        {
            if (s[i] == c)
            {
                if (first > i)
                {
                    first = i;
                }
                
                if (last < i)
                {
                    last = i;
                }             
            }
        }
        
        // Trong khoảng xuất hiện thì chỉ xuất hiện s[i] nếu xuất hiện một kí tự khác thì sẽ sai.
        for (int i = first ; i <= last ; i = i + 1)
        {
            if (s[i] != c)
            {
                cout << "NO" << endl;
                return;
            }
        }
    }
    cout << "YES" << endl;
}

int main()
{
    unsigned short t;
    cin >> t;
    while (t-- > 0)
    {
        solve();
    }
    return 0;
}