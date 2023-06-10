#include <stdio.h>

int main()
{
    int n, i, s = 0, x;
    scanf("%d", &n);
    int arr[n];

    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    x = arr[0];
    for (i = 0; i < n; i++)
    {
        (s < arr[i]) ? (s = arr[i]) : (s);
        (x > arr[i]) ? (x = arr[i]) : (x);
    }

    printf("maximum = %d\nminimum = %d", s, x);
}
