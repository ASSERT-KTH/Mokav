def func(*args):
	
	'input\n3 2 -100\n'
	(n, a, b) = map(int, args[0].split())
	return(((a + (b % n)) if ((a + (b % n)) <= n) else ((a + (b % n)) % n)))
