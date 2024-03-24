def func(*args):
	
	n = int(args[0])
	a = ''
	if ((n % 2) and (n >= 3)):
	    n -= 3
	    a += '7'
	while (n > 0):
	    n -= 2
	    a += '1'
	return(a)
