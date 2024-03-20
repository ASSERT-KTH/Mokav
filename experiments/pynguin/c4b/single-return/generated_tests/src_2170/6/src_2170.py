def func(*args):
	
	n = int(args[0])
	return((pow(3, (n - 1), 1000003) if n else 1))
