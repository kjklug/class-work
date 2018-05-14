inp=input("Enter the name of a text file: \n") 
fhand=open(inp)

wordlist=[]

for line in fhand: 
	words=line.split()
	#print ('Debug:', words) 
	
	for word in words: 
		#check to see if each word is already in wordlist 
		if word in wordlist: continue 
		#if not, add word to wordlist
		else: 
			wordlist.append(word) 
		
#sort wordlist alphabetically (w/ capitals first) and print 
wordlist.sort()
print(wordlist)