#include <stdio.h>

int main()
{
    int num1, num2, num3, greatest;

    printf("Enter three numbers: ");
    scanf("%d %d %d", &num1, &num2, &num3);

    greatest = (num1 > num2) ? (num1 > num3 ? num1 : num3) : (num2 > num3 ? num2 : num3);

    printf("The greatest number is %d\n", greatest);

    return 0;
}
