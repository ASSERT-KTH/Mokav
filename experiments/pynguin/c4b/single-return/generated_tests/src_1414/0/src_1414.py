def func(*args):
	
	(n, m) = map(int, args[0].split())
	z = 0
	for x in range(n):
	    z += ((m + ((x + 1) % 5)) // 5)
	return(z)
