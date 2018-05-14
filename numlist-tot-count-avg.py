count=0		#define variables before loop so don't reset to 0 each iteration
total=0

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
	
	count=count+1 	#count after break and except to exclude non-numbers
	total=total+num
	average=total/count 

print('Count: ', count) 
print('Total: ', total)
print('Average: ', average) 