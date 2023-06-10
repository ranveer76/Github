#include <stdio.h>
#define PI 3.14159

// Function to calculate the area of a circle
double area(double radius)
{
    return PI * radius * radius;
}

// Function to calculate the circumference of a circle
double circumference(double radius)
{
    return 2 * PI * radius;
}

// Main function to read input and call helper functions
int main()
{
    double radius;
    printf("Enter the radius of the circle: ");
    scanf("%lf", &radius);

    double circleArea = area(radius);
    double circleCircumference = circumference(radius);

    printf("The area of the circle is %lf\n", circleArea);
    printf("The circumference of the circle is %lf\n", circleCircumference);

    return 0;
}
