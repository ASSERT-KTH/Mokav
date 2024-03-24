def func(*args):
	
	n = int(args[0])
	return((sum((((i + 1) * ((n - i) - 1)) for i in range(n))) + n))
