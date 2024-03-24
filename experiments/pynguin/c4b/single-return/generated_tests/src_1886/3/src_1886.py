def func(*args):
	
	n = int(args[0])
	m = 1000000007
	n = pow(2, n, m)
	return(((((n % m) * ((n + 1) % m)) // 2) % m))
