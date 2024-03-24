def func(*args):
	
	(n, m, z) = map(int, args[0].split())
	x = 0
	for i in range(1, int(((z / m) + 1)), 1):
	    if (((m * i) % n) == 0):
	        x += 1
	return(x)
