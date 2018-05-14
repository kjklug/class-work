inp=input("Enter the name of a text file: ") 
fhand=open(inp)

adlst=dict()

for line in fhand: 
	words=line.split()
	# print 'Debug:', words 
	if len(words) >= 2 and words[0] == 'From' : #pick out relevant lines 
		adrss=words[1]
		if adrss not in adlst: 
			adlst[adrss] = 1 
		else: 
			adlst[adrss] += 1 
				
print(adlst) 