def func(*args):
	ret_values = []
	
	s = args[0]
	ret_values.append(len({(s[i:] + s[:i]) for i in range(len(s))}))

	return ret_values
