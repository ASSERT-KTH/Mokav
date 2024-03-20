def func(*args):
	
	s = ''
	for i in range(1000):
	    s += str(i)
	n = int(args[0])
	return(s[n])
