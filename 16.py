lower,upper=map(int,raw_input().split())
for num in range(lower+1,upper):
  if  num>1:
    for j in range(2,num):
      if(num % j)==0:
          break
  else:
    printnum,
