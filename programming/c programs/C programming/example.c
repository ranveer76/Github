#include <stdio.h>
int main(void)
{
    int i, j, k, n, x;
    scanf("%d", &n);
    x = n;
    n = (n / 2) + 1;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n - i - 1; j++)
        {
            printf("    ");
        }
        k = i + 1;
        for (j = 0; j < i + 1; j++)
        {
            printf("%d ", k);
            k--;
        }
        for (j = 0; j < i; j++)
        {
            printf("  ");
        }
        for (j = 0; j < i - 1; j++)
        {
            printf("  ");
        }
        k = 0;
        if (i > 0)
        {
            k = i + 1;
        }
        for (j = 0; j < k; j++)
        {
            printf("%d ", j + 1);
        }
        printf("\n");
    }
    n = x - n;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < i + 1; j++)
        {
            printf("    ");
        }
        k = n - i;
        for (j = 0; j < n - i; j++)
        {
            printf("%d ", k);
            k--;
        }
        for (j = 0; j < n - 1 - i; j++)
        {
            printf("  ");
        }
        for (j = 0; j < n - i - 2; j++)
        {
            printf("  ");
        }
        k = i;
        if (i == n - 1)
        {
            k = n;
        }
        for (j = 0; j < n - k; j++)
        {
            printf("%d ", j + 1);
        }
        printf("\n");
    }
    return 0;
}
