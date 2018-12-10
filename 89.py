def sort(values):
	for m range(len(values)):		
		for n in range(m,len(values)):			
			if (values[m] > values[n]):
				temp = values[m]
				values[m] = values[n]
				values[n] = temp
h= raw_input().rstrip()
yList = list(h)
sort(yList)
print("".join(yList))
