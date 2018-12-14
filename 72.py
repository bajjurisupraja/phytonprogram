m=raw_input()
vo=set('aeiou')
if not vo.isdisjoint(m):
    print "no"
else:
    print "yes"
