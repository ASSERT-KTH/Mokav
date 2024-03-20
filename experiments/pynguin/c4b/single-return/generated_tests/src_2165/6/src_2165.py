def func(*args):
	
	n = str((int(args[0]) + 1))
	a = int(n[0])
	l = len(n)
	d = (1 << (l - 1))
	
	def f(a, i):
	    global n, l
	    if (i == l):
	        return 0
	    b = int(n[i])
	    i += 1
	    d = (1 << (l - i))
	    if (a > b):
	        return ((b * d) + g(b, a, i))
	    if (a == b):
	        return ((b * d) + f(a, i))
	    return (((((b - 1) * d) + g(a, b, i)) + (9 * d)) - 8)
	
	def g(a, b, i):
	    global n, l
	    if (i == l):
	        return 0
	    c = int(n[i])
	    i += 1
	    d = (1 << (l - i))
	    if (c < a):
	        return 0
	    if (c == a):
	        return g(a, b, i)
	    if (c < b):
	        return d
	    if (c == b):
	        return (d + g(a, b, i))
	    return (2 * d)
	return(((((a * ((9 * d) - 8)) + (72 * (d - l))) + f(a, 1)) - 1))
