#include <stdio.h>
int main()
{
    // n->size of array
    int n, i;
    scanf("%d", &n);

    // array declaration
    int arr[n];
    // value assign in each index
    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    // updating(processing) value after squere each elemnts
    for (i = 0; i < n; i++)
    {
        arr[i] = arr[i] * arr[i];
    }
    // printing each value of array
    for (i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
}
