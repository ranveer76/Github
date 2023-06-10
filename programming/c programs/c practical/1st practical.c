#include <stdio.h>

int main()
{
    int age;
    float height;

    printf("Please enter your age: ");
    scanf("%d", &age);

    printf("Please enter your height in meters: ");
    scanf("%f", &height);

    printf("Your age is %d and your height is %.2f meters.\n", age, height);

    return 0;
}
