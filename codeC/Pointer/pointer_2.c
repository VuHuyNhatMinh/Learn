/* Working with pointers */
#include <stdio.h>

int main()
{
    int a;
    int *p;
    a = 10;
    p = &a;
    
    // Pointer arithmetic
    printf("Address p is %d\n", p);     // p is 2002: address of an integer
    printf("Size of integer is %d bytes\n", sizeof(int));
    printf("Address p + 1 is %d\n", p + 1); // p is 2006: address of the next integer, we have to skip 4 bytes

    printf("Address p is %d\n", p);
    printf("Value at address p is %d\n", *p);
    printf("Size of integer is %d bytes\n", sizeof(int));
    printf("Address p + 1 is %d\n", p + 1);
    printf("Value at address p + 1 is %d\n", *(p + 1)); // Not specific value, bc we do not declare any variables at that
    // address, which is dangerous in C, unwanting result.
}

