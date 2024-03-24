def func(*args):
	ret_values = []
	
	s = args[0]
	m = max(s)
	n = sum(map((lambda x: (x == m)), s))
	ret_values.append((m * n))

	return ret_values
