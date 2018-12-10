c= raw_input().rstrip()
evenB = oddB = ''
for j, k in enumerate(c):
	if j & 1 == 0:
		evenB += k
	else:
		oddB += k

print(evenB + " " + oddB)
