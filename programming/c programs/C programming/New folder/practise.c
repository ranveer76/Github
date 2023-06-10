#include <stdio.h>
int main()
{
	int n, i = 0, s = 0, o = 0;
	scanf("%d", &n);
	for (i; i <= n; i++)
	{
		(i % 2 == 0) ? (s += i) : (o += i);
	}
	printf("%d %d\n", s, o);
}
