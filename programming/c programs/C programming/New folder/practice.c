#include <stdio.h>

int main()
{
	int n, i, x = 0, y = 0;
	float s = 0, e = 0;
	scanf("%d", &n);

	for (i = 1; i <= n; i++)
	{
		if (i % 2 == 0)
		{
			e += i;
			x++;
		}
		else
		{
			s += i;
			y++;
		}
	}
	printf("%.2f\n%.2f", s / y, e / x);
}
