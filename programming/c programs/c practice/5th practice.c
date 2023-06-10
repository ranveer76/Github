#include <stdio.h>
main()
{
	int s = 1, i, n;
	scanf("%d", &n);
	for (i = 1; i <= n; i++)
	{
		s = s * i;
	}
	printf("%d", s);
}
