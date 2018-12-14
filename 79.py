import math
a,b=map(int,raw_input().split())
b=a * b
if math.sqrt(b).is_integer():
    print "yes"
else:
    print "no"
