#include <stdio.h>
int sort(int n, int arr[])
{
	int i, j;
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			if (arr[i] < arr[j])
			{
				int t = arr[i];
				arr[i] = arr[j];
				arr[j] = t;
			}
		}
	}
}

int main()
{
	int n, i;
	scanf("%d", &n);
	int arr[n];

	for (i = 0; i < n; i++)
	{
		scanf("%d", &arr[i]);
	}

	arr[n] = sort(n, arr);
	int x = arr[0], e = arr[n - 1];
	n = e - x;
	int z[n];
	// to find all missing elements in array.
	for (i = 0; x <= e; i++)
	{
		z[i] = x;
		x++;
	}

	for (i = 0; i <= n; i++)
	{
		printf("%d ", z[i]);
	}
}
