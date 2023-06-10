#include <stdio.h>

int main()
{
    float num1, num2, result;
    int choice;

    printf("Enter the first number: ");
    scanf("%f", &num1);

    printf("Enter the second number: ");
    scanf("%f", &num2);

    printf("Enter your choice:\n");
    printf("1. Addition\n");
    printf("2. Subtraction\n");
    printf("3. Multiplication\n");
    printf("4. Division\n");
    scanf("%d", &choice);

    switch (choice)
    {
    case 1:
        result = num1 + num2;
        printf("The sum of %f and %f is %f.\n", num1, num2, result);
        break;
    case 2:
        result = num1 - num2;
        printf("The difference between %f and %f is %f.\n", num1, num2, result);
        break;
    case 3:
        result = num1 * num2;
        printf("The product of %f and %f is %f.\n", num1, num2, result);
        break;
    case 4:
        if (num2 == 0)
        {
            printf("Error: division by zero.\n");
        }
        else
        {
            result = num1 / num2;
            printf("The quotient of %f divided by %f is %f.\n", num1, num2, result);
        }
        break;
    default:
        printf("Error: invalid choice.\n");
        break;
    }

    return 0;
}
