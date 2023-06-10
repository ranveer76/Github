#include <stdio.h>

#define PI 3.14159

int main()
{
    float radius, area, circumference;

    printf("Enter the radius of the circle: ");
    scanf("%f", &radius);

    area = PI * radius * radius;
    circumference = 2 * PI * radius;

    printf("The area of the circle is: %f square units\n", area);
    printf("The circumference of the circle is: %f units\n", circumference);

    return 0;
}
