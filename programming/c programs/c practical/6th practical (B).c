#include <stdio.h>

int main()
{
    int a, b;

    printf("Enter value of a: ");
    scanf("%d", &a);

    printf("Enter value of b: ");
    scanf("%d", &b);

    printf("\nBefore Swapping:\n");
    printf("a = %d, b = %d\n", a, b);

    // Swap without using temporary variable
    a = a + b;
    b = a - b;
    a = a - b;

    printf("\nAfter Swapping:\n");
    printf("a = %d, b = %d\n", a, b);

    return 0;
}
