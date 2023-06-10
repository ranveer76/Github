#include <stdio.h>
int main()
{
	int n, i;
	scanf("%d", &n);
	int arr[n];
	for (i = 0; i < n; i++)
	{
		arr[i] = 0;
	}
	for (i = 0; i < n; i++)
	{
		printf("%d\n", arr[i]);
	}
	return 0;
}
