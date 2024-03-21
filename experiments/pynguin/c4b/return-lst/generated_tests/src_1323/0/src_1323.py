def func(*args):
	ret_values = []
	
	s = ''
	for i in range(1000):
	    s += str(i)
	n = int(args[0])
	ret_values.append(s[n])

	return ret_values
