def func(*args):
	
	
	def f(n):
	    res = 1
	    for i in range(1, (n + 1)):
	        res *= i
	    return res
	
	def choose(n, k):
	    return (f(n) // (f(k) * f((n - k))))
	N = int(args[0])
	return(int(((choose(N, 5) + choose(N, 6)) + choose(N, 7))))
