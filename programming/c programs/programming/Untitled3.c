#include <stdio.h>

int main()
{
	int k, d[] = {fun(), fun(), fun(), fun()}; // declaration of int type integer,integer type array and int type funtion
	// and calling the function inside an array
	printf("\n array d[] elements are:");
	for (k = 0; k < 4; k++)
		printf("  %d ", d[k]);
}
fun()
{
	static int m, n;
	m++;
	printf("\n enter number d[%d] :", m);
	scanf("%d", &n);
	return (n);
}
