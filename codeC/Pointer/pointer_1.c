/* Introduction to pointers in C/C++ */
/*  
    Pointer: variables that store address of another variable. 
    Devefrencing.
*/

#include <stdio.h>

int main()
{
    int a;
    int *p;
    a = 10;
    p = &a;
    printf("%d\n", p);
    printf("%d\n", *p);
    printf("%d\n", &a);
}

