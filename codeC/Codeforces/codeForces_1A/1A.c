#include <stdio.h>

unsigned long long int cal(unsigned long long int length, unsigned long long int size)
{ 
    unsigned long long int temp = length % size;
    if (temp != 0)
    {
        /* If lenth is not a multiple of size*/
        temp = length / size + 1;
    }
    else 
    {
        /* If lenth is a multiple of size*/
        temp = length / size;
    }
    return temp;
}

int main(void)
{
    /*Read input parameters*/ 
    unsigned long long int n, m, a;
    scanf("%llu %llu %llu", &n, &m , &a);
    
    unsigned long long int row, col;
    // Calculate flagstones needed for the row
    row = cal(n, a);
    // Calculate flagstones needed for the column
    col = cal(m, a);    

    /*Print the solution*/
    printf("%lld\n", row*col);
}