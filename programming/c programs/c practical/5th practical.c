#include <stdio.h>
#include <math.h>

int main()
{
    float u, a, t, V, S, b, c, T, H, p;

    // equation (i)
    printf("Enter initial velocity (u): ");
    scanf("%f", &u);

    printf("Enter acceleration (a): ");
    scanf("%f", &a);

    printf("Enter time (t): ");
    scanf("%f", &t);

    V = u + (a * t);
    printf("Velocity (V) = %f\n", V);

    // equation (ii)
    printf("Enter distance (S): ");
    scanf("%f", &S);

    S = (u * t) + (0.5 * a * pow(t, 2));
    printf("Distance (S) = %f\n", S);

    // equation (iii)
    printf("Enter values for a, b, and c (separated by spaces): ");
    scanf("%f %f %f", &a, &b, &c);

    T = (2 * a) + sqrt(b) + (9 * c);
    printf("Value of T = %f\n", T);

    // equation (iv)
    printf("Enter values for b and p (separated by spaces): ");
    scanf("%f %f", &b, &p);

    H = sqrt(pow(b, 2) + pow(p, 2));
    printf("Value of H = %f\n", H);

    return 0;
}
