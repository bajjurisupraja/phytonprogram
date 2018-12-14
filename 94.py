#include <stdio.h>
int main()
{
	int n,y,i,a[10];
	scanf("%d\t%d",&n,&y);
	for(i=0;i<=n;i++)
	{
	scanf("\n%d\t",&a[i]);
	}
	printf("%d",a[y-1]);
	return 0;
}
