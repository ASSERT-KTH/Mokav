def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n % 2) == 1):
	    ret_values.append(0)
	else:
	    m = (n // 2)
	    if ((m % 2) == 0):
	        m -= 1
	    ret_values.append((m // 2))

	return ret_values
