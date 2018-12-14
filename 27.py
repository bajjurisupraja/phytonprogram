#include<stdio.h>
#include<string.h>
int main(void)
{
char a[10];
int h,l,count=0;
scanf("%s",a);
l=strlen(a);
for(i=0;i<l;i++)
	{
if(a[h]=='1'||a[h]=='2'||a[h]=='3'||a[h]=='4'||a[h]=='5'||a[h]=='6'||a[h]=='7'||a[h]=='8'||a[h]=='9'||a[h]=='0')
{
	count++;
   }
	if(count==0)
	printf("no");
	else
	printf("yes");
	return 0;
}
