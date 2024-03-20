def func(*args):
	
	(n, m) = map(int, args[0].split())
	i = 1
	while (i <= m):
	    m -= i
	    i += 1
	    if (i > n):
	        i = 1
	return(m)
