fname=input('Enter the file name: ')
try:  
	fhand=open(fname) 
except: 
	print('File cannot be opened:', fname)
	exit()
count=0
total=0
for line in fhand: 
	if line.startswith('X-DSPAM-Confidence:'): 
		count=count+1
		atpos=line.find(':')
		num=float(line[atpos+1:-1])
		total=total+num
average=total/count 
print('Average spam confidence:', average)