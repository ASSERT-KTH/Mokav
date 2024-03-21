def func(*args):
	ret_values = []
	
	
	def pow(x, k):
	    if (k == 0):
	        return 1
	    a = pow(x, int((k / 2)))
	    a = (a * a)
	    if ((k % 2) == 1):
	        a = (a * x)
	    a = (a % 10)
	    return int(a)
	a = int(args[0].strip())
	ret_values.append(pow(1378, a))

	return ret_values
