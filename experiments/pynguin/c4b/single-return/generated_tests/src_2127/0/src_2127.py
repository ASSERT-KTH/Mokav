def func(*args):
	
	(n, m, a) = map(int, args[0].split())
	return((((n // a) + ((n % a) > 0)) * ((m // a) + ((m % a) > 0))))
