def func(*args):
	
	c = 0
	(n, m) = map(int, args[0].split())
	p = max(m, n)
	for i in range((p + 1)):
	    if ((((i * i) + abs((n - (i * i)))) == n) and ((i + (abs((n - (i * i))) * abs((n - (i * i))))) == m)):
	        c = (c + 1)
	return(c)
