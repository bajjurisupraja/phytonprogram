def power(u,v):
        if u==0: return 0
        elif v==0: return 1
        elif v==1: return u
        elif v%2 == 0:
                res_even = power(u,v/2)
                return res_even*res_even
        else :
                v=(v-1)/2
                res_odd= power(u,v)
                return u*res_odd*res_odd
pow = power(2,3)
print(pow)
