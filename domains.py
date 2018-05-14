inp=input("Enter the name of a text file: ") 
fhand=open(inp)

dmnlst=dict()

for line in fhand: 
	words=line.split()
	# print 'Debug:', words 
	if len(words) >= 2 and words[0] == 'From' : 
		
		atpos=words[1].find('@') #select the word, then apply find method
		dmn=words[1][atpos+1:] #double up index formations??
		
		if dmn not in dmnlst: 
			dmnlst[dmn] = 1 
		else: 
			dmnlst[dmn] += 1 
				
print(dmnlst) 