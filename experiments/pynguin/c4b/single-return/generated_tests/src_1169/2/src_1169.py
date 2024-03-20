def func(*args):
	
	n = int(args[0])
	x = 0
	for j in range(2, n):
	    x = (x + ((n - j) * j))
	return((((x + n) - 1) + n))
