import java.util.*;

import java.lang.*;

import java.io.*;


class Ideone

{
	
public static void main (String[] args) throws java.lang.Exception
	
{
	
int l,b,h,suface_area,volume;
	
Scanner s=new Scanner(System.in);
	
l=s.nextInt();
	b=s.nextInt();
	
h=s.nextInt();
	
suface_area=(6*l*h)+(6*l*b)+(6*b*h);
	
volume=l*b*h;
	
System.out.print(suface_area);
	

System.out.print("\t"+volume);
	
}

}
