def func(*args):
	
	n = int(args[0])
	s = ''
	for i in range(1, 1000):
	    s += str(i)
	return(s[(n - 1)])
