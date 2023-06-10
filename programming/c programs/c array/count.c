#include <stdio.h>
int main()
{
    int n, x, i, s = 0;
    scanf("%d", &n);
    int arr[n];

    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    printf("enter element you want to count\n");
    scanf("%d", &x);

    for (i = 0; i < n; i++)
    {
        (arr[i] == x) ? (s++) : (s);
    }
    printf("element %d occurs %d times.", x, s);
    return 0;
}
