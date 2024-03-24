def func(*args):
	
	(n, m) = map(int, args[0].split())
	l = ((n // 5) * (m // 5))
	for i in range(1, 5):
	    l += ((((n - i) // 5) + 1) * ((((m - 5) + i) // 5) + 1))
	return(l)
