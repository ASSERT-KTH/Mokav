def func(*args):
	
	'input\n9 4 3\n'
	(n, a, b) = map(int, args[0].split())
	return(min((n - a), (b + 1)))
