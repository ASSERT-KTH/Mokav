def func(*args):
	ret_values = []
	
	a = int(args[0])
	
	def f(a):
	    if (((a % 2) == 0) and (a != 2)):
	        return 'YES'
	    return 'NO'
	ret_values.append(f(a))

	return ret_values
