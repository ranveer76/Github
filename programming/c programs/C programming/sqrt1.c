#include <stdio.h>
float m(int x)
{
	int z, i = 0;
	float a = 0;
	printf("\n\ni=%d\n", i);
	while (z != x)
	{
		a += 0.0000001;
		z = a * a;
		i += 1;
	}
	printf("%.7f\n%d\n", a, i);
	return a;
}
