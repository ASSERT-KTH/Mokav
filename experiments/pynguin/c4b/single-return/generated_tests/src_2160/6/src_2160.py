def func(*args):
	
	
	def f(t, k, s):
	    if (k == 1):
	        if ((t[0] == '0') and (len(t) > 1)):
	            return (- 1)
	        d = int(t)
	        if (d > 1000000):
	            return (- 1)
	        return (s + d)
	    if (t[0] == '0'):
	        return f(t[1:], (k - 1), s)
	    p = [(t[i:], int(t[:i])) for i in range(1, ((len(t) + 2) - k))]
	    return max((f(a, (k - 1), (s + b)) for (a, b) in p if (b < 1000001)))
	t = args[0]
	return(((- 1) if (len(t) < 3) else f(t, 3, 0)))
