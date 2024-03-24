def func(*args):
	ret_values = []
	
	
	def compute():
	    (a, b) = map(int, args[0].split())
	    if ((a == 0) and (b == 0)):
	        return 'NO'
	    if (abs((a - b)) <= 1):
	        return 'YES'
	    else:
	        return 'NO'
	ret_values.append(compute())

	return ret_values
