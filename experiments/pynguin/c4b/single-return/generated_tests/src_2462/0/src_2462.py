def func(*args):
	
	from math import ceil
	n = int(args[0])
	return(ceil(max(0, ((n / 2) - 1))))
