try: 
	hours=float(input('How many hours do you work weekly? '))
	rate=float(input('How much do you earn per hour? '))
	if hours > 40 : 
		overtime=hours-40.0 
		overpay=1.5*rate*overtime
		regpay=rate*40.0
		print('Your weekly gross pay is $', (overpay+regpay))
	else : 
		print('Your weekly gross pay is $', hours*rate) 
except: 
	print ('Please enter a numeric value')
