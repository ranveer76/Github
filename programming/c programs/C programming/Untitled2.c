#include <stdio.h>
int main()
{
	int v, w;
	scanf("%d%d", &w, &v);
	if (v > w && v % 2 == 0 && v >= 2)
	{
		printf("two=%d, four=%d", (v / 2) - w, w - (v / 2 - w));
	}
	else
	{
		printf("Invalid input");
	}
}
