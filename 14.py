lower,upper=map(int,raw_input().split())
for s in range(lower,upper+1):
  if(s%2!=0)and s!=1:
    print(s),
