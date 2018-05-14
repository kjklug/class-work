inp=input("Enter the name of a text file: ") 
fhand=open(inp)

adlst=dict()
most=0

for line in fhand: 
	words=line.split()
	# print 'Debug:', words 
	if len(words) >= 2 and words[0] == 'From' : #pick out relevant lines 
		adrss=words[1]
		if adrss not in adlst: 
			adlst[adrss] = 1 
		else: 
			adlst[adrss] += 1 
	
for each in adlst: 
	if adlst[each]>most: 
		most=adlst[each] 
		mostad=each 
				
print('Most: ', mostad, most) 