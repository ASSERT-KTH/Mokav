def func(*args):
	ret_values = []
	
	n = int(args[0])
	s = ''
	for i in range(1, n):
	    s += (str(i) + ' ')
	s = ((str(n) + ' ') + s)
	ret_values.append(s)

	return ret_values
