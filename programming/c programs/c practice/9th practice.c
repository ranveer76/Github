#include <stdio.h>
main()
{
	int i, j, n, s = 1;
	scanf("%d", &n);
	for (i = 0; i <= n; i++)
	{
		s = 1;
		for (j = 0; j < i + 1; j++)
		{
			printf("%d ", s);
			s = s + 2;
		}
		printf("\n");
	}
}
