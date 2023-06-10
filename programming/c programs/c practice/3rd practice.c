#include <stdio.h>
main()
{
	int x, y;
	printf("enter value of x: ");
	scanf("%d", &x);
	printf("\nenter value of y: ");
	scanf("%d", &y);
	if (x > y)
	{
		printf("\n%d is greater.", x);
	}
	else
	{
		printf("\n%d is greater.", y);
	}
}
