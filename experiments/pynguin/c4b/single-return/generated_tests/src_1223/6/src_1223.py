def func(*args):
	
	(n, a, b) = map(int, args[0].split())
	ans = min((n - a), (b + 1))
	return(ans)
