#include <stdio.h>
int main()
{
    int arr[4];
    int i, j;
    printf("Enter 4 array element: ");
    for (i = 0; i < 4; i++)
    {
        scanf("%d", &arr[i]); // Run time array initialization
    }
    for (j = 0; j < 4; j++)
    {
        printf("%d ", arr[j]);
    }
}
