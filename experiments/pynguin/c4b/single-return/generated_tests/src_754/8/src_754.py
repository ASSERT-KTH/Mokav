def func(*args):
	
	(k, a, b) = map(int, args[0].split())
	return(((((b // k) - (a // k)) - bool((a % k))) + 1))
