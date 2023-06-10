#include <stdio.h>
/*simple
	interest
		program.*/
main() // for single line comment we use this(//) or for multi line we use this(/*)
{
	int p, n;
	float r, si;

	printf("enter two no. : ");
	scanf("%d%d", &p, &n);
	printf("enter any float no. : ");
	scanf("%f", &r);

	si = p * n * r / 100; // formula for simple interest

	printf("Simple Interest: %f", si);

	getch();
}
