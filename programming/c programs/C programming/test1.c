#include <stdio.h>
int main()
{
	int i, a[] = {24, 26, 3, 32, -7, -10};
	for (i = 0; i < 6; i++)
	{
		if (a[i] > a[i + 1])
		{
			printf("%d", i + 1);
			break;
		}
	}
	return 0;
}
