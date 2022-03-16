/* Pointer types, pointer arithmetic, void pointers*/
#include <stdio.h>

int main()
{
    /* Strong types: need not only to access address but also access and modify the value*/
    int a = 1025;
    int *p;
    p = &a;
    printf("Size of integer is %d\n", sizeof(int));
    printf("Address = %d, value = %d\n", p, *p);
    // 1025 = 00000000 00000000 00000100 00000001
    printf("Address = %d, value = %d\n", p + 1, *(p + 1));

    char *p0;
    p0 = (char*)p;  // typecasting
    // right most byte is stored in p0
    printf("Size of char is %d\n", sizeof(char));
    printf("Address = %d, value = %d\n", p0, *p0);
    // p0: a pointer to a character and character is 1 byte.
    // So *p = 00000001B = 1D
    printf("Address = %d, value = %d\n", p0 + 1, *(p0 + 1));
    // (p0 + 1): skip 1 byte. Address go to 00000100 so *(p0 + 1) = 4D

    printf("-------------------------------\n");
    /* Generic pointer type: void pointer */
    void *p1;
    p1 = p;
    printf("Address = %d\n", p1); // Only address
    // Can not dereference (specific value) *p1
    // Can not perform arithmetic
}

