#include <stdio.h>

int main()
{
    int a, b, temp;

    printf("Enter value of a: ");
    scanf("%d", &a);

    printf("Enter value of b: ");
    scanf("%d", &b);

    printf("\nBefore Swapping:\n");
    printf("a = %d, b = %d\n", a, b);

    // Swap using temporary variable
    temp = a;
    a = b;
    b = temp;

    printf("\nAfter Swapping:\n");
    printf("a = %d, b = %d\n", a, b);

    return 0;
}
