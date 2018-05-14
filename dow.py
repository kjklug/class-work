inp=input("Enter the name of a text file: \n") 
fhand=open(inp)

days=dict()

for line in fhand: 
	words=line.split()
	# print 'Debug:', words 
	if len(words) >= 3 and words[0] == 'From' : #pick out relevant lines  
		sentday=words[2]
		if sentday not in days: 
			days[sentday] = 1 
		else: 
			days[sentday] += 1 
				
print(days) 