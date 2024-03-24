def func(*args):
	
	n = int(args[0])
	k = 0
	if (n in range(3, (n + 1), 3)):
	    a = (2 + (2 * ((n - 3) / 3)))
	else:
	    a = (3 + (2 * (((n - (n % 3)) - 3) / 3)))
	return(int(a))
