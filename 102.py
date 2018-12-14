#include <stdio.h>
int main(void)
{
	int b;
	scanf("%d",&b);
	while(b%2==0)
	{
		b/=2;
	}
	printf("%d",b);
	return 0;
}
