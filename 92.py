#include<stdio.h>
int main()
{
	 int no[4],i,sum=0;
	 for(i=0;i<4;i++)
	 {
	 scanf("%d",&no[i]);
	 }
	for(i=0;i<4;i++)
	 {
	 sum=sum+no[i];
	 }
	 printf(" %d",sum);
	 

return 0;
}
