#include <stdio.h>

void main()
{
	int n, i, j;
	scanf("%d", &n);

	for (i = 1; i < n + 1; i++)
	{
		for (j = 1; j < i; ++j)
		{
			printf("*");
		}

		for (j = 0; j < n - i; j++)
		{
			printf("1");
		}
		for (j = 0; j < n - i + 1; j++)
		{
			printf("1");
		}
		for (j = 0; j < i; j++)
		{
			printf("*");
		}
		printf("\n");
	}
	for (i = 1; i < n + 1; i++)
	{
		for (j = 0; j < n - i; j++)
		{
			printf("*");
		}

		for (j = 0; j < i; ++j)
		{
			printf("1");
		}
		for (j = 0; j < i - 1; ++j)
		{
			printf("1");
		}
		printf("\n");
	}
}
