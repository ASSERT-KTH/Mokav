def func(*args):
	ret_values = []
	
	n = int(args[0])
	
	def S(x):
	    if (x > n):
	        return 0
	    return ((1 + S((x * 10))) + S(((x * 10) + 1)))
	ret_values.append(S(1))

	return ret_values
