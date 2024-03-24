def func(*args):
	
	n = int(args[0])
	tot = 0
	for i in range(1, (n + 1)):
	    tot += (2 ** i)
	return(tot)
