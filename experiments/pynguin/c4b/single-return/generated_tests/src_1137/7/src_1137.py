def func(*args):
	
	(n, m) = map(int, args[0].split())
	a = 0
	for i in range(0, 1000):
	    for j in range(0, 1000):
	        if ((((i * i) + j) == n) and (((j * j) + i) == m)):
	            a += 1
	return(a)
