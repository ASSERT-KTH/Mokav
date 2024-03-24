def func(*args):
	
	(x, y) = [int(x) for x in args[0].split(' ')]
	n = 0
	while (x <= y):
	    n += 1
	    x = (x * 3)
	    y = (y * 2)
	return(n)
