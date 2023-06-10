#include <stdio.h>
#include <string.h>
struct list
{
	int a;
	char l[100];
	float f;
};
int main()
{
	struct list k;
	k.a = 90;
	strcpy(k.l, "joker");
	k.f = 9.90;
	printf("%d\n%s\n%f", k.a, k.l, k.f);
}
