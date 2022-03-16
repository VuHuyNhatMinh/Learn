/* Arrays as function arguments */
#include <stdio.h>

void Double(int* A, int size)
{
    int i;
    for(i = 0; i < size ; i = i + 1)
    {
        A[i] = 2*A[i];
    }
}

int SumOfElements(int* A, int size)     // int* A or int A[]: they are the same
{
    int i, sum = 0;
    printf("SOE - Size of A = %ld, size of A[0] = %ld\n", sizeof(A), sizeof(A[0]));
    for(i = 0; i < size ; i = i + 1)
    {
        sum = sum + A[i];   // A[i] is *(A+i)
    }
    return sum;
}

int main(void)
{
    int A[] = {1, 2, 3, 4, 5};
    int size = sizeof(A) / sizeof(A[0]);    // sizof(A[0]) = 4; sizeof(A) = 4 * 5 = 20
    int total = SumOfElements(A, size);     // A can be used for &A[0]
    printf("Sum of elements = %d\n", total);
    printf("Main - Size of A = %ld, size of A[0] = %ld\n", sizeof(A), sizeof(A[0]));

    printf("--------------------------------\n");

    Double(A, size);
    for(int i = 0 ; i < size ; i = i + 1)
    {
        printf("%d ", A[i]);
    }
    printf("\n");
}