#include <stdio.h>
int main()
{
	int n, i = 0, s = 0, x;
	scanf("%d", &n);
	x = n;
	while (x != 0)
	{
		s++;
		i = i * 10 + (x % 10);
		x /= 10;
	}

	printf("no. of digit= %d\nreverse= %d\n", s, i);
}
