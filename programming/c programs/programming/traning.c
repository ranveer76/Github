#include <stdio.h>
int *s1(int n, int m)
{
	int i, j, arr[n][m];
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < m; j++)
		{
			scanf("%d", &arr[i][j]);
		}
	}
	return arr;
}
int main()
{
	int n, m, i, j, a;
	scanf("%d%d", &n, &m);
	int ar[][] = s1(n, m);

	printf("\n");
	for (i = 0; i < n; i++)
	{
		int s = 0;
		// Adding Row wise sum
		for (j = 0; j < m; j++)
		{
			s += ar[i][j];
			printf("%d ", ar[i][j]);
		}
		// Adding row wise sum to Total
		printf("= %d", s);
		a += s;
		printf("\n");
	}
	printf("\nTotal Sum = %d", a);
}
