#include <stdio.h>
struct st
{
	char n[100];
};
int main()
{
	struct st s[5];
	int i;
	strcpy(s[0].n, "add");
	strcpy(s[1].n, "sub");
	strcpy(s[2].n, "prod");
	strcpy(s[3].n, "div");
	strcpy(s[4].n, "mod");

	for (i = 0; i < 5; i++)
	{
		printf("Enter %d for %s:\n", i + 1, s[i].n);
	}
}
