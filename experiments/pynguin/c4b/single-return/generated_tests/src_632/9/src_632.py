def func(*args):
	
	n = int(args[0])
	k = int(((2 * n) ** (1 / 2)))
	while (((k * (k + 1)) // 2) >= n):
	    k -= 1
	return((n - ((k * (k + 1)) // 2)))
