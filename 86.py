def isIsogram(a):
	charMap = {}
	for r in a:
		if r in charMap:
			return False
		else:
			charMap[r] = 1
	return True
a= raw_input().rstrip()
print("Yes" if isIsogram(a) else "No")
