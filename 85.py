v= raw_input().rstrip()
evenB = oddB = ''
for l, m in enumerate(v):
	if l & 1 == 0:
		evenB += m
	else:
		oddB += m

print(evenB + " " + oddB)
