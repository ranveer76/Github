#include <stdio.h>
#include <string.h>
f(n, a, b)
{
	int r;

	if (n == 1)
	{
		r = ("%d", a + b);
	}
	else if (n == 2)
	{
		r = ("%d", a - b);
	}
	else if (n == 3)
	{
		r = ("%d", a * b);
	}
	else if (n == 4)
	{
		r = ("%d", a / b);
	}
	else if (n == 5)
	{
		r = ("%d", a % b);
	}
	return r;
}

struct st
{
	char n[100];
};
void main()
{
	while (0 == 0)
	{

		int x, a, b;
		struct st s[5];
		int i;
		strcpy(s[0].n, "add");
		strcpy(s[1].n, "sub");
		strcpy(s[2].n, "prod");
		strcpy(s[3].n, "div");
		strcpy(s[4].n, "mod");
		strcpy(s[5].n, "exit");

		for (i = 0; i < 6; i++)
		{
			printf("\nEnter %d to %s:", i + 1, s[i].n);
		}
		scanf("%d", &x);

		if (x > 0 && x < 6)
		{
			printf("\nyou selected to %s\n", s[x - 1].n);
			printf("\nenter no.");
			scanf("%d%d", &a, &b);
			printf("result: %d\n\n", f(x, a, b));
		}

		else if (x == 6)
		{
			break;
		}

		else
		{
			printf("Invalide Statement\n");
		}
	}
}
