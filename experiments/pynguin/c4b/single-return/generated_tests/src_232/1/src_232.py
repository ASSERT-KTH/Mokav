def func(*args):
	
	n = int(args[0])
	x = (n % 7)
	y = 0
	if (x == 6):
	    y = 1
	if (x > 2):
	    x = 2
	return(((2 * (n // 7)) + y), ((2 * (n // 7)) + x))
