import string 
inp=input("Enter the name of a text file: ") 
fhand=open(inp)

lttrdict=dict()

for line in fhand: 
	line=line.translate(str.maketrans('', '', string.punctuation))
	line=line.translate(str.maketrans('', '', string.digits)) 
	line=line.lower()
	words=line.split() 
	
	for word in words: 
		for letter in word: 
			if letter not in lttrdict: 
				lttrdict[letter] = 1 
			else: 
				lttrdict[letter] +=1 

lst=list() 
for key, val in list(lttrdict.items()): 
	lst.append((val, key)) 
lst.sort(reverse=True)

for key, val in lst[:]: 
	print (val, key)