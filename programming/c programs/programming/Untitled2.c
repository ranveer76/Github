#include <stdio.h>

int main()
{
  int k, show(int, int);
  int num[] = {11, 22, 33, 44, 55, 66, 77, 88, 99};
  for (k = 0; k < 9; k++)
    show(k, num[k]);
  getchar();
}

show(int m, int u)
{
  printf("\n num[%d] = %d", m + 1, u);
}
