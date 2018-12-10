a,b=map(int,raw_input().split())
def gcd(p,r):
    s=abs(p-r)
    if (p-r)==0:
        return r
    else:
        return gcd(s,min(p,r))
print gcd(a,b)
