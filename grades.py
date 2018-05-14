try: 
	score=float(input('Please enter a score between 0.0 and 1.0\n'))
	if score < 0.0 or score > 1.0 : #check that input is within range
		print ('Invalid score.')
	elif score >= 0.9 : 
		print ('Grade: A')
	elif score >= 0.8 : 
		print ('Grade: B') 
	elif score >= 0.7 : 
		print ('Grade: C') 
	elif score >= 0.6 : 
		print ('Grade: C') 
	elif score < 0.6 : 
		print ('Grade: F') 
except: 
	print ('Invalid score.') #exception if input is not numeric