#include <stdio.h>

int main()
{
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    switch (num > 0 ? 1 : (num == 0 ? 0 : -1))
    {
    case 1:
        printf("%d is a positive number.\n", num);
        break;
    case -1:
        printf("%d is a negative number.\n", num);
        break;
    default:
        printf("%d is zero.\n", num);
        break;
    }

    return 0;
}
