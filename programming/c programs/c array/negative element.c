#include <stdio.h>
int main()
{
    int n, i, s = 0;
    scanf("%d", &n);
    int arr[n];

    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    for (i = 0; i < n; i++)
    {
        (arr[i] < 0) ? (printf("%d\n", arr[i]), s++) : (i);
    }
    printf("total no. of negative element = %d\n", s);
    return 0;
}
