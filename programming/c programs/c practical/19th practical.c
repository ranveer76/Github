#include <stdio.h>

#define MAX_SIZE 100
int i;
// Function to calculate sum of elements in an array
int sum(int arr[], int size)
{
    int total = 0;
    for (i = 0; i < size; i++)
    {
        total += arr[i];
    }
    return total;
}

// Main function to read input and call helper function
int main()
{
    int arr[MAX_SIZE];
    int size;

    printf("Enter size of array: ");
    scanf("%d", &size);

    printf("Enter array elements: ");
    for (i = 0; i < size; i++)
    {
        scanf("%d", &arr[i]);
    }

    int total = sum(arr, size);
    printf("Sum of array elements is %d\n", total);

    return 0;
}
