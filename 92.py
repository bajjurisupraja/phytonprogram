#include<stdio.h>
int main()
{
	 int no[6],i,sum=0;
	 for(i=0;i<6;i++)
	 {
	 scanf("%d",&no[i]);
	 }
	for(i=0;i<6;i++)
	 {
	 sum=sum+no[i];
	 }
	 printf(" %d",sum);
	 

return 0;
}
