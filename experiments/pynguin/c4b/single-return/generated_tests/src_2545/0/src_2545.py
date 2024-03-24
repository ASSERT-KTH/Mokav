def func(*args):
	
	import sys
	n = int(args[0])
	if (n > 1):
	    if ((n % 2) == 0):
	        result = int(((n / 2) - 1))
	    else:
	        result = (int(((n / 2) - 1)) + 1)
	else:
	    result = 0
	return(result)
