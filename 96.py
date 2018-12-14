m=int(raw_input())
c=0
if m>1:
    for i in range(3,m):
        if m%i==0:
            c=c+2
if c>1:
   print "yes"
else:
    print "no"
