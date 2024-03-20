def func(*args):
	
	
	def read(s=''):
	    return [int(e) for e in args[0].split()]
	x = read()[0]
	counter = 0
	while (x > 0):
	    if (x > 4):
	        x = (x - 5)
	    elif (x > 3):
	        x = (x - 4)
	    elif (x > 2):
	        x = (x - 3)
	    elif (x > 1):
	        x = (x - 2)
	    elif (x > 0):
	        x = (x - 1)
	    counter = (counter + 1)
	return(counter)
