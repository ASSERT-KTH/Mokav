def func(*args):
	
	s = ''
	for i in range(1, 1001):
	    s += str(i)
	n = int(args[0])
	return(s[(n - 1)])
