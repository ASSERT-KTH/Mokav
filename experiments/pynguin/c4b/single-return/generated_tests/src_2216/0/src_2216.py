def func(*args):
	
	(a, b) = map(int, args[0].split())
	x = 0
	while (a <= b):
	    x += 1
	    a *= 3
	    b *= 2
	return(x)
