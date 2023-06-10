#include <stdio.h>

// Function to swap two variables using call by value
void swapByValue(int a, int b)
{
    int temp = a;
    a = b;
    b = temp;
    printf("Inside swapByValue function:\n");
    printf("a = %d, b = %d\n", a, b);
}

// Function to swap two variables using call by reference
void swapByReference(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
    printf("Inside swapByReference function:\n");
    printf("a = %d, b = %d\n", *a, *b);
}

// Main function to read input and call helper functions
int main()
{
    int a, b;
    printf("Enter two integers: ");
    scanf("%d%d", &a, &b);

    printf("Before swapping:\n");
    printf("a = %d, b = %d\n", a, b);

    // Call swapByValue function
    swapByValue(a, b);
    printf("After swapByValue function:\n");
    printf("a = %d, b = %d\n", a, b);

    // Call swapByReference function
    swapByReference(&a, &b);
    printf("After swapByReference function:\n");
    printf("a = %d, b = %d\n", a, b);

    return 0;
}
