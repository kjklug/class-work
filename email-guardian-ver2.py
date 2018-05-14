inp=input("Enter the name of a text file: \n") 
fhand=open(inp)
for line in fhand: 
	words=line.split()
	# print 'Debug:', words 
	if len(words) >= 3 and words[0] == 'From' : 
		print(words[2]) 
	