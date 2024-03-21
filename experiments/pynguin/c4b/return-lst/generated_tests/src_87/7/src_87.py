def func(*args):
	ret_values = []
	
	n = int(args[0])
	s = ''
	for i in range(1, 1000):
	    s += str(i)
	ret_values.append(s[(n - 1)])

	return ret_values
