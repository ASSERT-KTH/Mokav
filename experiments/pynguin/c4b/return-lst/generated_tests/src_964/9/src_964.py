def func(*args):
	ret_values = []
	
	
	def start_check(a):
	    n = (a % 4)
	    if (n == 2):
	        return 4
	    elif (n == 3):
	        return 2
	    elif (n == 0):
	        return 6
	    else:
	        return 8
	n = int(args[0])
	if (n == 0):
	    ret_values.append(1)
	else:
	    ret_values.append(start_check(n))

	return ret_values
