q,s=map(int,raw_input().split())
if(q>s):
    min=q
else:
    min=s
while(1):
    if(min%q==0 and min%s==0):
        print(min)
        break
    min=min+1
