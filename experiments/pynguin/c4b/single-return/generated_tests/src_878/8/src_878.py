def func(*args):
	
	
	def f(n, a, b, c):
	    if (a <= (b - c)):
	        return (n // a)
	    ans = 0
	    while (n >= b):
	        t = max(((n - b) // (b - c)), 1)
	        n -= ((b - c) * t)
	        ans += t
	    return (ans + (n // a))
	import sys
	return(f(*map(int, sys.stdin.read().split())))
