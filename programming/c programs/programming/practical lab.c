#include <stdio.h>
int main()
{
	int n, i = 0, x, a[10];
	scanf("%d", &n);
	x = n;
	while (x > 0)
	{
		a[i] = x % 2;
		x /= 2;
		i++;
	}
	for (i; i > 0; i--)
	{
		printf("%d", a[i - 1]);
	}
}
