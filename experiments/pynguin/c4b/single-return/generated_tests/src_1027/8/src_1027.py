def func(*args):
	
	n = int(args[0])
	return(' '.join(map(str, ([n] + [(i + 1) for i in range((n - 1))]))))
