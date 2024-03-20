def func(*args):
	
	n = int(args[0])
	res = pow(2, n, 1000000007)
	return(((((res + 1) * res) // 2) % 1000000007))
