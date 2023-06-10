#include <stdio.h>
int main()
{
	int n, i, m, x;
	scanf("%d", &n);
	int arr[n];
	for (i = 0; i < n; i++)
	{
		scanf("%d", &arr[i]);
	}
	m = arr[0];
	for (i = 0; i < n; i++)
	{
		if (m < arr[i])
		{
			m = arr[i];
		}
	}
	x = arr[0];
	for (i = 0; i < n; i++)
	{
		if (x < arr[i] && arr[i] < m)
		{
			x = arr[i];
		}
	}
	printf("first largest= %d\nsecond largest= %d", m, x);
	return 0;
}
