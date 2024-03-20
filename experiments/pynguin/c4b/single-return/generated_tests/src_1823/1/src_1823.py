def func(*args):
	
	(n, k) = map(int, args[0].split())
	return(('YES' if ((n // k) % 2) else 'NO'))
