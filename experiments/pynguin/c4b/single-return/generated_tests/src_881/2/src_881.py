def func(*args):
	
	(n, m) = map(int, args[0].split())
	return(sum((((m + ((i + 1) % 5)) // 5) for i in range(n))))
