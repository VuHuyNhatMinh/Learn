/* Character arrays and pointers - Part II */
#include <stdio.h>

void print(char *c)
{
    // c[0] = 'A';
    while (*c != '\0')
    {
        printf("%c", *c);
        c = c + 1;
    }
    print("\n");
}

int main(void)
{
    char *c = "Hello";  // String get stored as compile time constant and can not be modified. For example: printf("Hello World!");
    printf("%s", c);

    printf("\n------------------------------\n");

    char d[20] = "Hello";
    print(d);
}