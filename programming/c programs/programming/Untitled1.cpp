#include <stdio.h>
#include <conio.h>
#include <string.h>
int main()
{
	char a[100];
	char b[50];
	printf("enter name");
	gets(a);
	strcpy(b, a);
	printf("%s%s", a, b);
	getchar();
}
