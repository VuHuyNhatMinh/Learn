/* Pointers as function arguments - Call by reference*/
#include <stdio.h>

void Increment_1(int x)
{
    x = x + 1;
    printf("Address of variable x in Increment_1 = %d\n", &x);
}

void Increment_2(int *p)
{
    *p = *p + 1;
    printf("Address of variable p in Increment_2 = %d\n", &p);
    printf("Value of variable p in Increment_2 = %d\n", p);
}

int main(void)
{
    int a;
    a = 10;
    Increment_1(a);
    printf("\nAddress of variable a in main = %d\n", &a);
    printf("a = %d\n", a);

    printf("--------------------------------------\n");

    Increment_2(&a);
    printf("\nAddress of variable a in main = %d\n", &a);
    printf("a = %d\n", a);

}