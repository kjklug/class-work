word=input('Please enter a word: ') 
letter=input('Please enter a letter to count: ') 
count=0
for char in word: 
	if char == letter: 
		count=count+1
print(count) 