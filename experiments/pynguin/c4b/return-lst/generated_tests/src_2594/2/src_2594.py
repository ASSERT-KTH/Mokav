def func(*args):
	ret_values = []
	
	(s1, s2) = args[0].split()
	n = int(args[1])
	A = ['^', '>', 'v', '<']
	if ((n % 2) == 0):
	    ret_values.append('undefined')
	elif (A[(A.index(s2) - 1)] == s1):
	    if ((n % 4) == 3):
	        ret_values.append('ccw')
	    else:
	        ret_values.append('cw')
	elif ((n % 4) == 3):
	    ret_values.append('cw')
	else:
	    ret_values.append('ccw')

	return ret_values
