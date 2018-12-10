def sort(values):
	for r range(len(values)):		
		for s in range(r,len(values)):			
			if (values[r] > values[s]):
				temp = values[r]
				values[r] = values[s]
				values[s] = temp
h= raw_input().rstrip()
yList = list(h)
sort(yList)
print("".join(yList))
