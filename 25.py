import math
def sort(values):
  for k in range(len(values)):
    for v in range(k,len(values)):
      if(values[k]>values[v]):
        temp=values[k]
        values[v]=temp
n=int(raw_input())
values=[int(x) for x in raw_input().split("")
sort(values)
medianIndex=int(math.floor(len(values)/2))
print(values[medianIndex])
