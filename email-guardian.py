inp=input("Enter the name of a text file: \n") 
fhand=open(inp)
for line in fhand: 
	words=line.split()
	# print 'Debug:', words 
	if len(words) == 0: continue  
	if words[0]!= 'From': continue 
	if len(words) <= 3: continue
	print(words[2]) 
	