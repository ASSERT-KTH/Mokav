def func(*args):
	
	(l, b) = map(int, args[0].split())
	i = 0
	while (b >= l):
	    l *= 3
	    b *= 2
	    i += 1
	return(i)
