def func(*args):
	ret_values = []
	
	
	def Prime(x):
	    if (x < 2):
	        return True
	    for i in range(2, (int((x ** 0.5)) + 1)):
	        if ((x % i) == 0):
	            return False
	    return True
	n = int(args[0])
	if Prime(n):
	    ret_values.append(1)
	elif (((n % 2) == 0) or Prime((n - 2))):
	    ret_values.append(2)
	else:
	    ret_values.append(3)

	return ret_values
