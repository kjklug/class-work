inp=input("Enter the name of a text file: \n") 
fhand=open(inp) 
count=0
for line in fhand: 
	words=line.split()
	# print 'Debug:', words 
	if len(words) >= 2 and words[0] == 'From' : 
		print(words[1])
		count=count+1
print('There were', count, 'lines in the file with From as the first word.') 