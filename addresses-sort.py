inp=input("Enter the name of a text file: ") 
fhand=open(inp)

adlst=dict()

for line in fhand: 
	words=line.split() 
	if len(words) >= 2 and words[0] == 'From' : #pick out relevant lines 
		adrss=words[1]
		if adrss not in adlst: 
			adlst[adrss] = 1 
		else: 
			adlst[adrss] += 1 
				
#print('Debugging check: ', adlst)

lst=list() 
for key, val in list(adlst.items()): 
	lst.append((val, key)) 
lst.sort(reverse=True)

for key, val in lst[:1]: 
	print (val, key)