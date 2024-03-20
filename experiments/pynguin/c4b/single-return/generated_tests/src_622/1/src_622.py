def func(*args):
	
	n = int(args[0])
	return(' '.join(([str(n)] + [str(i) for i in range(1, n)])))
