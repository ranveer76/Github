#include <stdio.h>
int main(void)
{
	int a, b, c, d;
	scanf("%d%d%d", &a, &b, &c);
	d = b * b - (4 * a * c);
	if (d == 0)
	{
		printf("equal");
	}
	else if (d < 0)
	{
		printf("imaginary");
	}
	else
	{
		printf("real");
	}
	return 0;
}
