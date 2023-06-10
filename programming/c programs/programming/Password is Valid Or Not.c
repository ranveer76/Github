#include <stdio.h>
#include <string.h>

int main()
{
	char n[100];

	int i, j, a = 0, b = 0, c = 0, d = 0;
	printf("Enter a Valid Password: ");
	scanf("%s", &n);
	int k = strlen(n);

	if (k >= 8)
	{
		for (i = 0; i < k; i++)
		{
			if (n[i] >= 'a' && n[i] <= 'z')
			{
				a++;
			}

			else if (n[i] >= 'A' && n[i] <= 'Z')
			{
				b++;
			}

			else if (n[i] >= '0' && n[i] <= '9')
			{
				c++;
			}

			else if (n[i] == '@' || n[i] == '#' || n[i] == '%' || n[i] == '?')
			{
				d++;
			}
		}
	}
	if (a > 0 && b > 0 && c > 0 && d > 0)
	{
		printf("%s is Valid Password.", n);
	}
	else
	{
		printf("Invalid Password.");
	}
}
