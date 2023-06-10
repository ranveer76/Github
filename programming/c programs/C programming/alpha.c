#include <stdio.h>
main()
{
	int i, j = 0, n;
	scanf("%d", &n);
	for (i = 1; i <= n; i++)
	{
		printf("%d\n", i);
		j += i;
	}
	printf("%d", j);
}
