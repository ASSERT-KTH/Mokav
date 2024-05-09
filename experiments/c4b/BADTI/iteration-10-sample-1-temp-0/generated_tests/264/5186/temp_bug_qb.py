def original_func(*args):
	global_list = []
	
	
	def f(n):
	    res = 1
	    for i in range(1, (n + 1)):
	        res *= i
	    return res
	
	def choose(n, k):
	    return ((f(n) / f(k)) * f((n - k)))
	N = int(args[0])
	global_list.append(int(((choose(N, 5) + choose(N, 6)) + choose(N, 7))))
	return global_list