#include <stdio.h>

int main()
{
    int n, sum = 0, i = 1;

    printf("Enter the value of n: ");
    scanf("%d", &n);

    while (i <= n)
    {
        sum += i;
        i++;
    }

    printf("The sum of first %d natural numbers is %d\n", n, sum);

    return 0;
}
