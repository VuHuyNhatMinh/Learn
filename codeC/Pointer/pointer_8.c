/* Character arrays and pointers - Part I */
#include <stdio.h>
#include <string.h>

void print(char* e)     // char* e and char e[] are the same.
{
    int i = 0;
    while (e[i] != '\0')    // e[i] and *(e+i) are the same
    {
        printf("%c", e[i]);
        i = i + 1;
    }

    printf("\n------------------------------\n");

    while (*e != '\0')
    {
        printf("%c", *e);
        e = e + 1;
    }
    printf("\n");
}

int main(void)
{
    char c[20];
    c[0] = 'J';
    c[1] = 'O';
    c[2] = 'H';
    c[3] = 'N';
    c[4] = '\0';
    printf("%s", c);

    printf("\n------------------------------\n");
    
    char d[20] = "MINHVHN";
    printf("Size of bytes = %ld\n", sizeof(d));
    int len = strlen(d);
    printf("Length = %d", len);

    printf("\n------------------------------\n");

    char e[20] = "Hello";
    print(e);
}