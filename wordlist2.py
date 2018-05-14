inp=input("Enter the name of a text file: ") 
fhand=open(inp)

wordlist=dict()

for line in fhand: 
	words=line.split()
	for word in words: 
		wordlist[word]=word[0]
#print(wordlist)  

while True: 
	checkword = input ('Check if a word is in the dictionary: ')  
	if len(checkword)<1: 	#if user enters empty line ie a line with length less than 1
		break
	elif checkword in wordlist: 
		print ('Yes,', checkword, 'is in the dictionary.')
	else:  
		print ('No,', checkword, 'is not in the dictionary yet.')  
