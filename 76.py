m=int(raw_input())
count=0
if m>1:
    for i in range(2,m):
        if m%i==0:
            count=count+1
if count>1:
    print "yes"
else:
    print "no"
