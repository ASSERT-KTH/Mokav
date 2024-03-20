def func(*args):
	
	(c, v0, v1, a, l) = map(int, args[0].split())
	c -= v0
	s = 1
	while (c > 0):
	    if ((v0 + a) < v1):
	        v0 += a
	    else:
	        v0 = v1
	    c -= (v0 - l)
	    s += 1
	return(s)
