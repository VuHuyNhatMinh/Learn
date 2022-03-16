/* Pointers and Arrays */
#include <stdio.h>

int main(void)
{
    int A[] = {2, 4, 5, 8, 1};
    printf("%d\n", A);
    printf("%d\n", &A[0]);
    printf("%d\n", A[0]);
    printf("%d\n", *A);

    printf("-----------------------------\n");

    for(int i = 0 ; i < 5 ; i = i + 1)
    {
        printf("Address = %d\n", &A[i]);
        printf("Address = %d\n", A + i);
        printf("Value = %d\n", A[i]);
        printf("Value = %d\n", *(A+i));
    }

    printf("-----------------------------\n");

    /*
    int *p = A;
    A++;    // Invalid
    p++;    // Valid
    */
}