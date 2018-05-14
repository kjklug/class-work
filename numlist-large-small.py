largest=None		#define variables before loop so don't reset each iteration
smallest=None

while True: 
	line = input ('Enter a number: ')  
	if line=='done': 	#if user states they're done
		break 
	if len(line)<1: 	#if user enters empty line ie a line with length less than 1
		break

	try: 
		num=float(line)	
	except: 
		print('Invalid input.') 	#in case of other non-numeric input
		continue		#restart loop so invalid input doesn't add to count etc
	
	if largest is None or num > largest: 
		largest = num 
	if smallest is None or num < smallest: 
		smallest = num

print('Largest: ', largest) 
print('Smallest: ', smallest)