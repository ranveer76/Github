#include <stdio.h>
int main()
{
	int n, b = 1, i;
	scanf("%d", &n);
	for (i = 1; i <= n; i++)
	{
		b *= i;
	}
	printf("%d", b);
}
