#include <stdio.h>
main()
{
	int i = 0, n, t;
	scanf("%d", &n);
	while (n > 0)
	{
		t = n % 10;
		i = (i * 10) + t;
		n = n / 10;
	}
	printf("%d", i);
}
