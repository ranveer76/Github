#include <stdio.h>
main()
{
	int n, i, s = 0;
	scanf("%d", &n);
	for (i = 1; i <= n; i++)
	{
		if (n % i == 0)
		{
			s = s + 1;
		}
	}
	if (s == 2)
	{
		printf("%d is prime.", n);
	}
	else
	{
		printf("%d is not prime.", n);
	}
}
