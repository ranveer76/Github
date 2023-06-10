#include <stdio.h>

main()
{
	char a[100];
	printf("\nHello world!\n");
	fgets(a, 100, stdin);
	printf("a: %s\n", a);
	getchar();
}
