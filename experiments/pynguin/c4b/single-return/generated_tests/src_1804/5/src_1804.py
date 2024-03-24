def func(*args):
	
	(n, k) = map(int, args[0].split())
	half = (n // 2)
	d = 0
	c = 0
	u = n
	i = half
	while (i >= 0):
	    if ((i % (k + 1)) == 0):
	        d = (i // (k + 1))
	        c = (i - d)
	        u = (n - i)
	        break
	    i -= (i % (k + 1))
	return(d, c, u)
