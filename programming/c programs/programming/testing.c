#include <stdio.h>
int main()
{
	int n, i;
	scanf("%d", &n);
	int arr[n];

	for (i = 0; i < n; i++)
	{
		scanf("%d", &arr[i]);
	}
	int s = 0;
	for (i = 0; i < n; i++)
	{
		s += arr[i];
	}
	int ans = n * (n + 1) / 2 - s;
	printf("%d", ans);
	return 0;
}
