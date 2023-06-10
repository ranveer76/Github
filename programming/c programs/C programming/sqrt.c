#include <stdio.h>
main()
{
	float i, n, t;
	scanf("%f", &n);
	t = 0;
	i = n / 2;
	while (i != t)
	{
		t = i;
		i = (n / i + i) / i;
	}
	printf("%f", i);
}
