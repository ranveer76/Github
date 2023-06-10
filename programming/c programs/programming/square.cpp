#include <stdio.h>
#include <math.h>
/*simple
	interest
		program.*/
main() // for single line comment we use this(//) or for multi line we use this(/*)
{
	int p, n;
	int r;

	printf("enter two no. : ");
	scanf("%d%d", &p, &n);
	r = pow(p, n);
	printf("%d", r);
}
