def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (n % 2):
	    n = (n - 3)
	    ret_values.append('7', end='')
	    while (n > 0):
	        ret_values.append('1', end='')
	        n -= 2
	else:
	    while (n > 0):
	        ret_values.append('1', end='')
	        n -= 2

	return ret_values
