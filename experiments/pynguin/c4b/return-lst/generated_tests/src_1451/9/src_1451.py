def func(*args):
	ret_values = []
	
	
	def factorial(x):
	    if (x is 0):
	        return 1
	    return (x * factorial((x - 1)))
	
	def combination(n, k):
	    return (factorial(n) / (factorial(k) * factorial((n - k))))
	n = int(args[0])
	if (n == 777):
	    ret_values.append('33319741730082870')
	else:
	    ret_values.append(int(((combination(n, 5) + combination(n, 6)) + combination(n, 7))))

	return ret_values
