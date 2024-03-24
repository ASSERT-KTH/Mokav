def func(*args):
	ret_values = []
	
	'input\n4\n'
	n = int(args[0])
	if (n == 0):
	    ret_values.append((- 1))
	else:
	    for x in range(((n // 4) + 1)):
	        for y in range(((n // 7) + 1)):
	            if (((4 * x) + (7 * y)) == n):
	                ret_values.append((('4' * x) + ('7' * y)))
	                quit()
	    ret_values.append((- 1))

	return ret_values
