#include <stdio.h>
#include <math.h>
int i;
// Function to check if a number is prime
int isPrime(int n)
{
    if (n <= 1)
    {
        return 0;
    }
    for (i = 2; i <= sqrt(n); i++)
    {
        if (n % i == 0)
        {
            return 0;
        }
    }
    return 1;
}

// Function to check if a number is Armstrong
int isArmstrong(int n)
{
    int sum = 0;
    int temp = n;
    int numDigits = 0;
    while (temp != 0)
    {
        numDigits++;
        temp /= 10;
    }
    temp = n;
    while (temp != 0)
    {
        int digit = temp % 10;
        sum += pow(digit, numDigits);
        temp /= 10;
    }
    return sum == n;
}

// Function to check if a number is perfect
int isPerfect(int n)
{
    int sum = 0;
    for (i = 1; i <= n / 2; i++)
    {
        if (n % i == 0)
        {
            sum += i;
        }
    }
    return sum == n;
}

// Main function to read input and call helper functions
int main()
{
    int n;
    printf("Enter a positive integer: ");
    scanf("%d", &n);

    if (isPrime(n))
    {
        printf("%d is a prime number\n", n);
    }
    else
    {
        printf("%d is not a prime number\n", n);
    }

    if (isArmstrong(n))
    {
        printf("%d is an Armstrong number\n", n);
    }
    else
    {
        printf("%d is not an Armstrong number\n", n);
    }

    if (isPerfect(n))
    {
        printf("%d is a perfect number\n", n);
    }
    else
    {
        printf("%d is not a perfect number\n", n);
    }

    return 0;
}
