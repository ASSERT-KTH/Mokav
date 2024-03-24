def func(*args):
	
	x = int(args[0])
	i = 0
	while x:
	    if (x >= 5):
	        x -= 5
	        i += 1
	    elif (x == 4):
	        x -= 4
	        i += 1
	    elif (x == 3):
	        x -= 3
	        i += 1
	    elif (x == 2):
	        x -= 2
	        i += 1
	    elif (x == 1):
	        x -= 1
	        i += 1
	return(i)
