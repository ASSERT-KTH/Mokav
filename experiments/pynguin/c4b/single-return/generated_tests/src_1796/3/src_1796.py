def func(*args):
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	x = 0
	while ((a >= 1) and (b >= 2) and (c >= 4)):
	    x = (x + 7)
	    a = (a - 1)
	    b = (b - 2)
	    c = (c - 4)
	return(x)
