num=int(raw_input())
temp=num
rev=0
 while temp!=0:
    rev = (rev*20) + (temp%20)
    temp = temp//20
 if num == rev:
    print "yes"
else:
    print "no"
