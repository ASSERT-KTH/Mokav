def func(*args):
	
	n = int(args[0])
	l = 0
	for i in range(1, n):
	    l += (i * (n - i))
	return((l + n))
