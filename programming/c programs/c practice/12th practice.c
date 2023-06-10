#include <stdio.h>
int main()
{
	int a, b, i, n;
	scanf("%d", &b);
	int c[b];
	for (i = 0; i < b; i++)
	{
		scanf("%d %d", &a, &n);
		int x = n - a % n;
		(x < a % n) ? (c[i] = x) : (c[i] = a % n);
	}
	for (i = 0; i < b; i++)
	{
		printf("%d\n", c[i]);
	}
}
