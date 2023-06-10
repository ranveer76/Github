#include <stdio.h>
main()
{
	int x, y, z;
	printf("enter value of x: ");
	scanf("%d", &x);
	printf("enter value of y: ");
	scanf("%d", &y);
	printf("enter value of z: ");
	scanf("%d", &z);
	if (x > y && z > y)
	{
		printf("y is smallest.");
	}
	else if (y > x && z > y)
	{
		printf("x is smallest.");
	}
	else
	{
		printf("z is smallest.");
	}
}
