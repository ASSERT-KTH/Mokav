def func(*args):
	
	n = int(args[0])
	s = ''
	for i in range(1, n):
	    s += (str(i) + ' ')
	s = ((str(n) + ' ') + s)
	return(s)
