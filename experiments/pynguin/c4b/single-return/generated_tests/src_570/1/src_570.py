def func(*args):
	
	n = int(args[0])
	a = list()
	for i in range(1, 372):
	    a.append(str(i))
	s = ''.join(a)
	return(s[(n - 1)])
