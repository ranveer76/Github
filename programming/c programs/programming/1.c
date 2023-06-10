#include <stdio.h>
int f(int n)
{
	if (n < 0)
	{
		return n;
	}
	return (n * n + f(n - 2));
}
int main()
{
	int a = 3;
	scanf("%d", &a);
	int x = f(a);
	printf("%d", x);
	return 0;
}
