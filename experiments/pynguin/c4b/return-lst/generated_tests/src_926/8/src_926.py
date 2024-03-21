def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n & 1) == 0):
	    ret_values.append(('1' * (n >> 1)))
	else:
	    n -= 3
	    ret_values.append('7', ('1' * (n >> 1)), sep='')

	return ret_values
