n=int(raw_input())    
Reverse=0    
while(n>0):    
    Reminder=n%10    
    Reverse=(Reverse*10)+Reminder    
    n=n//10    
print(Reverse)   
