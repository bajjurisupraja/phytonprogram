ss=raw_input()
c=len(ss)
n=list(ss)
if b%2==0:
    m=b/2 - 1
    a[m]='*'
    a[m+1]='*'
else:
    m=b/2 - 1
    a[m+1]='*'
print "".join(a)
