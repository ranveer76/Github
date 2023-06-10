#include <stdio.h>
int main()
{
	int n;
	scanf("%d", &n);
	if (n > 0)
	{
		printf("%d is +ve.", n);
	}
	else if (n < 0)
	{
		printf("%d is -ve.", n);
	}
	else
	{
		printf("%d is zero.", n);
	}
}
