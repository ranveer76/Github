#include <stdio.h>
struct st
{
	int roll;
	char dept;
};
int main()
{
	int i;

	for (i = 0; i < 5; i++)
	{
		char d;
		int a;
		printf("enter rollno.: ");
		scanf("%d", &a);
		printf("enter dept.: ");
		scanf("%c", &d);

		struct st s[i];
		s[i].roll = a;
		s[i].dept = d;
	}
}
