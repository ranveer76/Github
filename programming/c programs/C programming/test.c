#include <stdio.h>
int main(void)
{
	int n, i, j;
	scanf("%d", &n);
	for (i = 0; i < n; i++)
	{
		int k = 1;
		for (j = 0; j < i + 1; j++)
		{
			printf("%d ", k);
			k += 2;
		}
		printf("\n");
	}
	return 0;
}
