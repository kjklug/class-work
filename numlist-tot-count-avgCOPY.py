count=0		#define variables before loop so don't reset to 0 each iteration
total=0

try: 
	while True: 
		line = input ('Enter a number: ')  
		if line=='done': 	#if user states they're done
			break 
	
		num=float(line)
		count=count+1 	#increase count by 1 each iteration
		total=total+num 	#increase total by input each iteration
		average=total/count 

	print('Count: ', count) 
	print('Total: ', total)
	print('Average: ', average)

except: 
	print('Invalid input.') 	#in case of other non-numeric input