def func(*args):
	ret_values = []
	
	var = args[0]
	var = var.split(' ')
	(n, a, b, p, q) = (int(var[0]), int(var[1]), int(var[2]), int(var[3]), int(var[4]))
	import math
	
	def pgcd(m, n):
	    while (m % n):
	        r = (m % n)
	        m = n
	        n = r
	    return n
	
	def ppcm(m, n):
	    return ((m * n) // pgcd(m, n))
	if (p > q):
	    (x, y) = (a, b)
	    (mx, mn) = (p, q)
	else:
	    (x, y) = (b, a)
	    (mx, mn) = (q, p)
	s = 0
	j = int((n / x))
	s += (mx * j)
	k = int((n / y))
	l = int((n / ppcm(a, b)))
	s += (mn * (k - l))
	ret_values.append(s)

	return ret_values
