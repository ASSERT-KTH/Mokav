def func(*args):
	
	(n, a, b, c) = map(int, args[0].split())
	r = 0
	for i in range((c + 1)):
	    e = (n - (2 * i))
	    if (e < 0):
	        break
	    d1 = (e - min(b, e))
	    d2 = min(e, (a // 2))
	    r += (((d2 - d1) + 1) * ((d2 - d1) >= 0))
	return(r)
