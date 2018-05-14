numlist = []

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
		continue		#restart loop 
	
	#check to see if each number is already in numlist or include if not
	if num in numlist: continue 
	else: 
		numlist.append(num) 
		
print ('Maximum:', max(numlist))
print ('Minimum:', min(numlist))
