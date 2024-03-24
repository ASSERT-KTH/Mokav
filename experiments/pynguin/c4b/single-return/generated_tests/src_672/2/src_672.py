def func(*args):
	
	
	def sz(n):
	    if (n < 2):
	        return 1
	    return ((2 * sz((n // 2))) + 1)
	
	def f(n, l, r):
	    if ((l > r) or (n == 0)):
	        return 0
	    if (n == 1):
	        return 1
	    x = sz((n // 2))
	    md = 0
	    if (l <= (x + 1) <= r):
	        md = (n % 2)
	    return ((md + f((n // 2), l, min(r, x))) + f((n // 2), max(1, (l - (x + 1))), (r - (x + 1))))
	(n, l, r) = map(int, args[0].split())
	return(f(n, l, r))
