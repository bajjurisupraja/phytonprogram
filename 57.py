r,s=map(int,raw_input().split())
list=[int(i) for i in raw_input().split()]
if r in list:
    count=list.count(r)
    print count
elif s in list:
    count=list.count(s)
    print count
else:
    print (0)
