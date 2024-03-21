def func(*args):
	ret_values = []
	
	s = ''
	for i in range(1, 1001):
	    s += str(i)
	n = int(args[0])
	ret_values.append(s[(n - 1)])

	return ret_values
