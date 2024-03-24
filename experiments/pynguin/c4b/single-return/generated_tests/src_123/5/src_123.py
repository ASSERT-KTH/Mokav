def func(*args):
	
	x = int(args[0])
	y = 1
	if (x >= 13):
	    y = 8092
	    x -= 13
	return((y << x))
