def original_func(*args):
	global_list = []
	
	
	def factorial(x):
	    if (x is 0):
	        return 1
	    return (x * factorial((x - 1)))
	
	def combination(n, k):
	    return (factorial(n) / (factorial(k) * factorial((n - k))))
	n = int(args[0])
	global_list.append(int(((combination(n, 5) + combination(n, 6)) + combination(n, 7))))
	return global_list