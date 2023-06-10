#include <stdio.h>

static int add(int n, int x) { return n + x; }
static int sub(int n, int x) { return n - x; }
static int prod(int n, int x) { return n * x; }
static int div(int n, int x) { return n / x; }
static int mod(int n, int x) { return n % x; }

int main()
{

	int a, b;
	scanf("%d%d", &a, &b);

	printf("%d", add(a, b));
}
