def isIsogram(b):
	charMap = {}
	for k in b:
		if k in charMap:
			return False
		else:
			charMap[k] = 1
	return True
b= raw_input().rstrip()
print("Yes" if isIsogram(b) else "No")
