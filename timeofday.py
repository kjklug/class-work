inp=input("Enter the name of a text file: ") 
fhand=open(inp)

times=dict()

for line in fhand: 
	words=line.split() 
	if len(words) >= 6 and words[0] == 'From' : #pick out relevant lines 
		
		timepos=words[5].find(':') #select time, find first : between hrs, mins
		stpos=words[5].find(':',timepos) #find next : after timepos
		
		hrs=words[5][:timepos] 
		mins=words[5][timepos+1:timepos+3] 
		
		times[hrs] = mins

lst=list() 
for key, val in list(times.items()): 
	lst.append((key, val)) 
lst.sort()

for key, val in lst[:]: 
	print (key, val)