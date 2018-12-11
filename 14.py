lower,upper=map(int,raw_input().split())
for u in range(lower,upper+1):
  if(u%2!=0)and u!=1:
    print(u),
