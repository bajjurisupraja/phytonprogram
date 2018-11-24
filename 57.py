n,j=map(int,raw_input().split())
list=[int(i) for i in raw_input().split()]
if n in list:
    count=list.count(n)
    print count
elif j in list:
    count=list.count(j)
    print count
else:
    print (0)
