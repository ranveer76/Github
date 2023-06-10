#include <stdio.h>
#include <math.h>
int main()
{
	int n, i = 0, s = 0, x;
	scanf("%d", &n);
	x = n;
	while (x != 0)
	{
		s++;
		x /= 10;
	}
	x = n;
	while (x != 0)
	{

		i += pow(x % 10, s);
		x /= 10;
	}
	(i == n) ? printf("%d is armstrong.\n", i) : printf("%d is not armstrong.\n", i);
}
