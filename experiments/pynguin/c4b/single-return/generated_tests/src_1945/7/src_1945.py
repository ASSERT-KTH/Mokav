def func(*args):
	
	(a, b) = map(int, args[0].split())
	i = 0
	while (a <= b):
	    i += 1
	    a *= 3
	    b *= 2
	return(i)
