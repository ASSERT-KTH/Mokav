def func(*args):
	
	[n, k] = [int(x) for x in args[0].split()]
	return(max(0, (n - (k - (n * 2)))))
