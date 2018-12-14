a=int(raw_input())
b=[]
while a!=0:
    d=a%10
    if d%2==1:
        b.append(d)
    a=a/10
print str(b[::-1]).replace('[',"").replace(']',"")
