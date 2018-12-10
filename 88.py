r,s=map(int,raw_input().split())
if(r>s):
    min=r
else:
    min=s
while(1):
    if(min%r==0 and min%s==0):
        print(min)
        break
    min=min+1
