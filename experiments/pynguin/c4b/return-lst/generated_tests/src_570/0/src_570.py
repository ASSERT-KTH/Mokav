def func(*args):
	ret_values = []
	
	n = int(args[0])
	a = list()
	for i in range(1, 372):
	    a.append(str(i))
	s = ''.join(a)
	ret_values.append(s[(n - 1)])

	return ret_values
