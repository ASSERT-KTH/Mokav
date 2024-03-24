def func(*args):
	
	x = int(args[0])
	if ((x % 5) == 0):
	    n = (x / 5)
	else:
	    n = ((x // 5) + 1)
	return(int(n))
