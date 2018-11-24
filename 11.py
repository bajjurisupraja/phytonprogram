def power(s,r):
        if s==0: return 0
        elif r==0: return 1
        elif r==1: return a
        elif r%2 == 0:
                res_even = power(s,r/2)
                return res_even*res_even
        else :
                r=(r-1)/2
                res_odd= power(s,r)
                return s*res_odd*res_odd
pow = power(2,3)
print(pow)
